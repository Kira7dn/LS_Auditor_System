from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / ".agents/skills/common/pdf-to-kb"


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, SKILL_ROOT / relative_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_repo_module(name: str, relative_path: str):
    return load_module(name, relative_path)


def test_postprocess_items_suppresses_heading_cluster_without_type_error() -> None:
    extractor = load_module("extract_pdf_to_kb", "scripts/extract_pdf_to_kb.py")
    cfg = extractor.DEFAULT_FONT_CONFIG.copy()

    result = extractor.postprocess_items(
        [
            ("h3", "A"),
            ("h3", "Beta"),
            ("h3", "Gamma"),
            ("h3", "Delta"),
            ("h3", "Epsilon"),
            ("h3", "Zeta"),
            ("body", "real body"),
        ],
        cfg,
    )

    assert result[:3] == [("body", "A Beta"), ("body", "Gamma Delta"), ("body", "Epsilon Zeta")]


def test_anchor_regex_accepts_single_double_quotes_and_spacing(tmp_path: Path) -> None:
    importer = load_module("import_concept_map", "scripts/import_concept_map.py")

    assert importer.has_anchor('<a id="scope_3"></a>', "scope_3")
    assert importer.has_anchor("<a   id = 'scope_3'   ></a>", "scope_3")
    assert importer.has_anchor('<a class="x" id="scope_3"></a>', "scope_3")


def test_resolve_doc_file_matches_numbered_markdown(tmp_path: Path) -> None:
    importer = load_module("import_concept_map", "scripts/import_concept_map.py")
    target = tmp_path / "04_oper_boundaries.md"
    target.write_text("# Operational Boundaries\n", encoding="utf-8")

    assert importer.resolve_doc_file(tmp_path, "oper_boundaries") == target


def test_file_uri_uses_actual_kb_dir_not_hardcoded_path(tmp_path: Path) -> None:
    importer = load_module("import_concept_map", "scripts/import_concept_map.py")
    target = tmp_path / "01_principles.md"
    target.write_text("# Principles\n", encoding="utf-8")

    file_uri = importer.file_uri_for_anchor(target, "principles_relevance")

    assert "Projects/ESG/ghg_kb" not in str(target.resolve())
    assert file_uri.endswith("#principles_relevance")
    assert target.resolve().as_uri() in file_uri


def test_import_scope_source_id_falls_back_when_metadata_missing() -> None:
    importer = load_module("import_concept_map_scope", "scripts/import_concept_map.py")

    assert importer.metadata_source_id({"source_id": "source_a"}, "fallback") == "source_a"
    assert importer.metadata_source_id({}, "fallback") == "fallback"


def test_import_infers_collection_from_kb_root(tmp_path: Path) -> None:
    importer = load_module("import_concept_map_collection", "scripts/import_concept_map.py")
    md = tmp_path / "ghg_protocol" / "04_oper_boundaries.md"
    md.parent.mkdir()
    md.write_text("# Operational Boundaries\n", encoding="utf-8")

    assert importer.collection_id_for_file(tmp_path, md, "fallback") == "ghg_protocol"
    assert importer.collection_id_for_file(md.parent, md, "fallback") == "fallback"


def test_query_node_payload_includes_scope_fields() -> None:
    query_graph = load_module("query_graph_scope", "scripts/query_graph.py")

    class FakeNode:
        labels = {"Concept", "Requirement"}

        def __init__(self) -> None:
            self.values = {
                "id": "scope_1",
                "name": "Scope 1",
                "project_id": "esg",
                "collection_id": "ghg_protocol",
                "source_id": "ghg_protocol_corporate_standard",
            }

        def get(self, key: str):
            return self.values.get(key)

    payload = query_graph.node_payload(FakeNode())

    assert payload["project_id"] == "esg"
    assert payload["collection_id"] == "ghg_protocol"
    assert payload["source_id"] == "ghg_protocol_corporate_standard"


def test_query_evidence_markdown_includes_pdf_highlight_image() -> None:
    query_graph = load_module("query_graph_evidence", "scripts/query_graph.py")

    evidence = query_graph.evidence_markdown(
        [
            {
                "anchor": "scope_3",
                "file_uri": "file:///kb.md#scope_3",
                "matched_text": "Scope 3 is an optional reporting category.",
            }
        ],
        [
            {
                "anchor": "scope_3",
                "page_number": 27,
                "bbox": [1, 2, 3, 4],
                "highlight_uri": "file:///highlight.png",
                "ambiguous": False,
            }
        ],
        5,
    )

    assert evidence[0]["pdf_highlight_uri"] == "file:///highlight.png"
    assert evidence[0]["pdf_highlight_markdown"] == "![PDF highlight](file:///highlight.png)"
    assert "PDF: page 27" in evidence[0]["markdown"]


def test_local_search_uses_fts_and_returns_citation(tmp_path: Path) -> None:
    query_graph = load_module("query_graph", "scripts/query_graph.py")
    md = tmp_path / "04_oper_boundaries.md"
    md.write_text('<a id="scope_3"></a>\nScope 3\n## Scope 3 emissions are optional but relevant.\n', encoding="utf-8")

    matches = query_graph.local_search(tmp_path, "Scope 3", 5)

    assert matches
    assert matches[0]["file"] == "04_oper_boundaries.md"
    assert matches[0]["citation"]["matched_text"] == "## Scope 3 emissions are optional but relevant."
    assert matches[0]["citation"]["anchor"] == "scope_3"
    assert matches[0]["content"] != "Scope 3"


def test_local_search_falls_back_to_token_fts_for_long_legal_query(tmp_path: Path) -> None:
    query_graph = load_module("query_graph_token_fallback", "scripts/query_graph.py")
    md = tmp_path / "04_oper_boundaries.md"
    md.write_text(
        '<a id="scope_1"></a>\nGHG emissions not covered by the Kyoto Protocol shall not be included in scope 1.\n',
        encoding="utf-8",
    )

    matches = query_graph.local_search(tmp_path, "not covered by the Kyoto Protocol shall not be included in scope 1", 5)

    assert matches
    assert matches[0]["citation"]["anchor"] == "scope_1"


def test_validate_citations_reports_anchor_mismatch(tmp_path: Path) -> None:
    validator = load_module("validate_citations", "scripts/validate_citations.py")
    md = tmp_path / "04_oper_boundaries.md"
    md.write_text('<a id="scope_1"></a>\n## Scope 1\n', encoding="utf-8")

    issues = validator.validate_node(
        {
            "id": "scope_1",
            "doc_id": "oper_boundaries",
            "anchor": "scope-1-direct-ghg-emissions",
            "file_path": str(md),
        },
        tmp_path,
        strict_metadata=False,
    )

    assert issues == ["scope_1: anchor 'scope-1-direct-ghg-emissions' not found in 04_oper_boundaries.md"]


def test_apply_preserved_anchors_reinserts_anchor_before_matching_heading() -> None:
    extractor = load_module("extract_pdf_to_kb", "scripts/extract_pdf_to_kb.py")
    old_content = '<a id="scope_1"></a>\n## Scope 1: Direct GHG emissions\nOld text\n'
    new_content = "## Scope 1: Direct GHG emissions\nNew text\n"

    result = extractor.apply_preserved_anchors(new_content, old_content)

    assert result.startswith('<a id="scope_1"></a>\n## Scope 1: Direct GHG emissions')


def test_auto_section_graph_extracts_scope_anchor_as_node(tmp_path: Path) -> None:
    importer = load_module("import_concept_map", "scripts/import_concept_map.py")
    md = tmp_path / "04_oper_boundaries.md"
    md.write_text(
        "\n".join(
            [
                "---",
                "id: oper_boundaries",
                'title: "Operational Boundaries"',
                'source_pdf: "source.pdf"',
                "page_start: 27",
                "page_end: 36",
                'content_hash: "abc"',
                "---",
                "",
                '<a id="scope_1"></a>',
                "## Scope 1: Direct GHG emissions",
            ]
        ),
        encoding="utf-8",
    )

    chapter, sections, edges = importer.extract_sections_from_markdown(md, tmp_path)

    assert chapter["id"] == "oper_boundaries"
    assert sections[0]["id"] == "scope_1"
    assert sections[0]["label"] == "ScopeRule"
    assert sections[0]["name"] == "Scope 1: Direct GHG emissions"
    assert edges == [{"from": "oper_boundaries", "to": "scope_1", "type": "CONTAINS", "edge_key": "oper_boundaries|CONTAINS|scope_1"}]


def test_llm_section_extraction_and_candidate_validation(tmp_path: Path) -> None:
    extractor = load_module("extract_llm_entities", "scripts/extract_llm_entities.py")
    validator = load_module("validate_llm_candidates", "scripts/validate_llm_candidates.py")
    md = tmp_path / "04_oper_boundaries.md"
    md.write_text(
        "\n".join(
            [
                "---",
                "id: oper_boundaries",
                'title: "Operational Boundaries"',
                'source_pdf: "source.pdf"',
                "page_start: 27",
                "page_end: 36",
                'content_hash: "abc"',
                "---",
                "",
                '<a id="scope_1"></a>',
                "## Scope 1: Direct GHG emissions",
                "Companies report GHG emissions from sources they own or control as scope 1.",
            ]
        ),
        encoding="utf-8",
    )

    sections = extractor.iter_anchored_sections(tmp_path, 8000)
    assert sections[0]["anchor"] == "scope_1"
    assert "Companies report" in sections[0]["text"]

    record = {
        "_line_number": 1,
        "doc_id": "oper_boundaries",
        "file": str(md),
        "anchor": "scope_1",
        "source_pdf": "source.pdf",
        "page_start": 27,
        "page_end": 36,
        "content_hash": "abc",
        "section_text_hash": sections[0]["section_text_hash"],
        "section_text": sections[0]["text"],
        "nodes": [
            {
                "id": "scope_1_direct_emissions",
                "label": "ScopeRule",
                "name": "Scope 1 direct emissions",
                "evidence_quote": "sources they own or control as scope 1",
                "confidence": 0.9,
            }
        ],
        "edges": [],
    }
    assert validator.validate_record(record, tmp_path) == []

    record["nodes"][0]["confidence"] = 0.0
    assert "confidence below minimum" in validator.validate_record(record, tmp_path)[0]


def test_llm_candidate_validator_allows_pdf_hyphen_line_break() -> None:
    validator = load_module("validate_llm_candidates_hyphen", "scripts/validate_llm_candidates.py")

    assert validator.quote_in_text(
        "geographic locations, industry sector",
        "geographic loca-\n\ntions, industry sector",
    )


def test_graph_quality_analysis_flags_duplicates_and_citation_gaps() -> None:
    analyzer = load_repo_module("analyze_graph_quality", "scripts/analyze_graph_quality.py")
    nodes = [
        {
            "id": "scope_1",
            "name": "Scope 1",
            "labels": ["Concept", "ScopeRule"],
            "file_uri": "file:///kb.md#scope_1",
            "anchor": "scope_1",
            "source_pdf": "source.pdf",
            "page_start": 1,
            "page_end": 1,
            "content_hash": "abc",
            "llm_generated": False,
            "auto_generated": False,
            "source_map_hash": "expert",
        },
        {
            "id": "scope_1_llm",
            "name": "Scope 1",
            "labels": ["Concept", "Requirement"],
            "file_uri": "file:///kb.md#scope_1",
            "anchor": "scope_1",
            "source_pdf": "source.pdf",
            "page_start": 1,
            "page_end": 1,
            "content_hash": "abc",
            "llm_generated": True,
            "auto_generated": False,
            "source_map_hash": "llm:abc",
        },
        {
            "id": "orphan_req",
            "name": "Missing Evidence",
            "labels": ["Concept", "Requirement"],
            "file_uri": "",
            "anchor": "",
            "source_pdf": "",
            "page_start": None,
            "page_end": None,
            "content_hash": "",
            "llm_generated": False,
            "auto_generated": False,
            "source_map_hash": "expert",
        },
    ]
    relationships = [
        {
            "from_id": "scope_1_llm",
            "to_id": "scope_1",
            "type": "APPLIES_TO",
            "llm_generated": True,
            "auto_generated": False,
            "confidence": 0.7,
        }
    ]

    report = analyzer.analyze(nodes, relationships, 0.86)

    assert report["summary"]["exact_duplicate_name_group_count"] == 1
    assert report["summary"]["expert_llm_overlap_count"] == 1
    assert report["summary"]["citation_gap_count"] == 1
    assert report["summary"]["orphan_requirement_count"] == 1


def test_llm_importer_loads_canonical_alias_file(tmp_path: Path) -> None:
    importer = load_module("import_llm_candidates_aliases", "scripts/import_llm_candidates.py")
    alias_file = tmp_path / "canonical_aliases.json"
    alias_file.write_text(
        '{"aliases": {"requirement_accuracy": "accuracy", "noop": "noop"}}',
        encoding="utf-8",
    )

    assert importer.load_aliases(str(alias_file)) == {"requirement_accuracy": "accuracy"}

    records = [
        {
            "nodes": [{"id": "requirement_accuracy"}, {"id": "scope_1"}],
            "edges": [{"from": "requirement_accuracy", "to": "scope_1", "type": "APPLIES_TO"}],
        }
    ]
    assert importer.summarize_records(records, {"requirement_accuracy": "accuracy"}, False) == {
        "skipped_records": 0,
        "nodes_imported": 1,
        "nodes_aliased": 1,
        "edges_imported": 1,
    }


def test_retrieval_eval_scores_concept_anchor_and_complete_citation() -> None:
    evaluator = load_repo_module("run_retrieval_eval", "scripts/run_retrieval_eval.py")
    payload = {
        "results": [{"id": "scope_1"}],
        "citations": [
            {
                "anchor": "scope_1",
                "file_uri": "file:///kb.md#scope_1",
                "source_pdf": "source.pdf",
                "page_start": 1,
                "page_end": 1,
                "content_hash": "abc",
            }
        ],
    }

    score = evaluator.score_result(payload, ["scope_1"], ["scope_1"])

    assert score["top_1_hit"] is True
    assert score["top_5_hit"] is True
    assert score["anchor_hit"] is True
    assert score["concept_hit"] is True
    assert score["citation_complete"] is True


def test_answer_guardrail_refuses_without_complete_citation() -> None:
    answer = load_repo_module("answer_question", "scripts/answer_question.py")

    refused = answer.answer_from_payload(
        "Scope 1 là gì?",
        {"query_metadata": {}, "citations": [{"matched_text": "Scope 1 direct emissions", "anchor": "scope_1"}]},
    )
    assert refused["refused"] is True

    accepted = answer.answer_from_payload(
        "Scope 1 là gì?",
        {
            "query_metadata": {},
            "citations": [
                {
                    "matched_text": "Scope 1 emissions are direct GHG emissions.",
                    "file_uri": "file:///kb.md#scope_1",
                    "anchor": "scope_1",
                    "source_pdf": "source.pdf",
                    "page_start": 1,
                    "page_end": 1,
                    "content_hash": "abc",
                }
            ],
        },
    )
    assert accepted["refused"] is False
    assert accepted["claims"][0]["citation"]["anchor"] == "scope_1"

    unsupported = answer.answer_from_payload(
        "xyz-no-evidence",
        {
            "query_metadata": {},
            "citations": [
                {
                    "matched_text": "Verification requires appropriate evidence.",
                    "file_uri": "file:///kb.md#verification",
                    "anchor": "verification",
                    "source_pdf": "source.pdf",
                    "page_start": 1,
                    "page_end": 1,
                    "content_hash": "abc",
                }
            ],
        },
    )
    assert unsupported["refused"] is True
    assert unsupported["reason"] == "unsupported_query_tokens"


def test_manifest_hash_and_uri_mask(tmp_path: Path) -> None:
    manifest = load_repo_module("write_run_manifest", "scripts/write_run_manifest.py")
    target = tmp_path / "file.txt"
    target.write_text("abc", encoding="utf-8")

    assert manifest.sha256_file(target) == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert manifest.mask_uri("neo4j+s://177d8aab.databases.neo4j.io") == "neo4j+s://177d***"


def test_pdf_bbox_resolver_matches_scope_anchor_and_cache_name() -> None:
    bbox = load_repo_module("pdf_bbox_citations", "scripts/pdf_bbox_citations.py")
    citations = [
        {
            "project_id": "esg",
            "collection_id": "ghg_protocol",
            "source_id": "ghg_protocol_corporate_standard",
            "anchor": "scope_1",
            "matched_text": "Scope 1 direct emissions",
        }
    ]
    index = [
        {
            "project_id": "esg",
            "collection_id": "ghg_protocol",
            "source_id": "ghg_protocol_corporate_standard",
            "anchor": "scope_1",
            "source_pdf": "source.pdf",
            "page_number": 27,
            "bbox": [1.0, 2.0, 3.0, 4.0],
            "matched_pdf_text": "Scope 1: Direct GHG emissions",
            "confidence": 0.95,
        }
    ]

    resolved = bbox.resolve_pdf_citations(citations, index)

    assert resolved[0]["anchor"] == "scope_1"
    assert resolved[0]["page_number"] == 27
    assert bbox.highlight_file_name(resolved[0]).startswith("ghg_protocol_corporate_standard__scope_1__p27__")


def test_highlight_file_name_uses_multi_bbox_hash() -> None:
    bbox = load_repo_module("pdf_bbox_citations_multi", "scripts/pdf_bbox_citations.py")
    record = {
        "source_id": "source",
        "anchor": "anchor",
        "page_number": 1,
        "bbox": [1, 2, 3, 4],
        "bboxes": [[1, 2, 3, 4], [5, 6, 7, 8]],
    }

    single = dict(record)
    single.pop("bboxes")
    assert bbox.highlight_file_name(record) != bbox.highlight_file_name(single)


def test_answer_claims_attach_pdf_citation_by_anchor() -> None:
    answer = load_repo_module("answer_question_pdf_bbox", "scripts/answer_question.py")
    claims = [{"claim": "Scope 1 direct emissions", "citation": {"anchor": "scope_1"}}]

    enriched = answer.attach_pdf_citations(claims, [{"anchor": "scope_1", "page_number": 27}])

    assert enriched[0]["pdf_bbox_missing"] is False
    assert enriched[0]["pdf_citation"]["page_number"] == 27


def test_query_legal_rag_wrapper_hides_project_pdf_bbox_defaults() -> None:
    wrapper = load_repo_module("query_legal_rag", "scripts/query_legal_rag.py")

    args = __import__("argparse").Namespace(
        preset="ghg",
        id=None,
        search="scope 1",
        mode=None,
        depth=1,
        limit=5,
        full_json=False,
        no_pdf_bbox=False,
        no_render_highlights=False,
    )

    command = wrapper.build_command(args)

    assert "--kb-dir" in command
    assert "Projects/ESG/kb/ghg_protocol" in command
    assert "--project-id" in command
    assert "esg" in command
    assert "--collection-id" in command
    assert "ghg_protocol" in command
    assert "--source-id" in command
    assert "ghg_protocol_corporate_standard" in command
    assert "--with-pdf-bbox" in command
    assert "--render-highlights" in command
    assert "--search" in command


def test_answer_legal_rag_wrapper_sets_bbox_defaults() -> None:
    wrapper = load_repo_module("answer_legal_rag", "scripts/answer_legal_rag.py")

    args = __import__("argparse").Namespace(
        preset="ghg",
        question="Scope 1 là gì?",
        limit=8,
        claim_limit=3,
        no_pdf_bbox=False,
        no_render_highlights=False,
    )

    command = wrapper.build_command(args)

    assert "--with-pdf-bbox" in command
    assert "--render-highlights" in command
    assert "--question" in command
    assert "Scope 1 là gì?" in command


def test_import_legal_rag_wrapper_uses_global_map_and_kb_root() -> None:
    wrapper = load_repo_module("import_legal_rag", "scripts/import_legal_rag.py")

    args = __import__("argparse").Namespace(
        preset="esg",
        prune_stale=False,
        no_auto_sections=False,
        full_json=False,
    )

    command = wrapper.build_command(args)

    assert "Projects/ESG/graph/concept_map.json" in command
    assert "Projects/ESG/kb" in command
    assert "Projects/ESG/kb/ghg_protocol" not in command
    assert "--strict-citation" in command


def test_build_citation_index_wrapper_hides_bbox_index_flags() -> None:
    wrapper = load_repo_module("build_citation_index", "scripts/build_citation_index.py")

    args = __import__("argparse").Namespace(preset="ghg")

    command = wrapper.build_command(args)

    assert "Projects/ESG/kb/ghg_protocol" in command
    assert "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl" in command
    assert "--source-id" in command


def test_pdf_citation_index_prefers_paragraph_for_duplicate_heading() -> None:
    builder = load_repo_module("build_pdf_citation_index", "scripts/build_pdf_citation_index.py")

    candidates = builder.candidate_texts(
        {
            "heading": "Scope 3: Other indirect GHG emissions",
            "paragraph": "Scope 3 is optional, but it provides an opportunity to be innovative in GHG management.",
            "duplicate_heading": True,
        }
    )

    assert candidates[0][0] == "paragraph"
    assert candidates[0][2] > candidates[1][2]
