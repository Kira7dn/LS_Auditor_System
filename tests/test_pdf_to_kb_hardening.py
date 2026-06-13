from __future__ import annotations

import importlib.util
from pathlib import Path


SKILL_ROOT = Path("C:/Users/kira7/.gemini/config/skills/pdf-to-kb")


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, SKILL_ROOT / relative_path)
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
