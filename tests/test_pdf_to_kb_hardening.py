from __future__ import annotations

import importlib.util
from pathlib import Path


SKILL_ROOT = Path("C:/Users/kira7/.gemini/config/skills/pdf-to-kb")
REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, SKILL_ROOT / relative_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_repo_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / relative_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
