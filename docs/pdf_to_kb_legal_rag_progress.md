# PDF-to-KB Legal RAG Progress Roadmap

Last updated: 2026-06-14

## 1. Current Position

The `pdf-to-kb` pipeline has moved beyond a demo/toy RAG system. It now has:

- PDF extraction into structured Markdown KB.
- Stable Markdown anchors for citation.
- Source metadata in Markdown frontmatter: `source_pdf`, `page_start`, `page_end`, `content_hash`.
- Deterministic section graph from Markdown headings and anchors.
- Expert-curated `concept_map.json` imported as the final enhancement/override layer.
- Neo4j graph ingestion with batch/source hashes and stale handling.
- Graph + local fulltext retrieval through `query_graph.py`.
- Staged LLM graph extraction through OpenAI API:
  - extract candidates,
  - validate evidence/citation/ontology/confidence,
  - import only validated candidate items.

Current maturity estimate:

| Area | Current maturity | Notes |
|---|---:|---|
| PDF to Markdown citation | 70% | Has file/page/hash/anchor, but not PDF bbox or paragraph-level page spans. |
| Graph ingestion safety | 85% | Idempotent import, citation validator, source hashes, stale handling, and applied canonical aliases. |
| Retrieval | 80-85% | Graph + FTS5 with token fallback; measured Top-5 hit rate is 0.85 on the first GHG eval set. |
| LLM graph extraction | 70% | Validated and useful; initial canonicalization is applied, but generic LLM nodes remain. |
| Citation integrity | 85% | `validate_citations` passes and answer prototype refuses unsupported/no-citation cases. |
| Legal-grade prototype readiness | 85-90% | Good enough for internal prototype use on current GHG KB, not yet production legal-grade. |

Practical conclusion: this is now a legal-grade prototype for the current GHG KB, not yet a production legal-grade system.

## 2. Latest Verified State

Environment:

- Project root: `D:/BusinessAnalyze/LS/LS_Auditor_System`
- Skill root: `C:/Users/kira7/.gemini/config/skills/pdf-to-kb`
- KB: `Projects/ESG/kb/ghg_protocol`
- Expert concept map: `Projects/ESG/graph/concept_map.json`
- Neo4j URI used by scripts: from `.env`
- Graph scope: `project_id=esg`, `collection_id=ghg_protocol`, `source_id=ghg_protocol_corporate_standard`

Current project layout:

```text
Projects/ESG/
  sources/
    ghg_protocol_corporate_standard/
      pdf/
      raw/
      manifest.source.json
    tcvn_iso_14064_1_2025/
      pdf/
      manifest.source.json
    tcvn_iso_14064_2_2025/
      pdf/
      manifest.source.json
    tcvn_iso_14067_2020/
      pdf/
      manifest.source.json
    inbox/
  kb/
    ghg_protocol/
  graph/
    concept_map.json
    canonical_aliases.json
    citation_reports/
    import_reports/
    llm_candidates/
    quality_reports/
  eval/
  manifests/
  archive/
```

`concept_map.json` remains the expert overlay for the current graph. New PDFs should first become a dedicated `sources/<source_id>/` collection with its own source manifest, then extract into `kb/<collection>/`; do not place source PDFs or generated graph artifacts directly in the project root.

Neo4j scoping status:

- `project_id`, `collection_id`, and `source_id` are now set on all current GHG `Concept` nodes and relationships.
- Import, query, citation validation, graph quality, retrieval eval, answer guardrail, alias apply, and run manifest accept scope parameters.
- Current graph has `0` nodes and `0` relationships missing these scope fields.
- Remaining v2 work: `Concept.id` is still globally unique, so multiple projects with overlapping IDs need scoped IDs or a composite uniqueness migration before importing another domain such as Accounting.

Latest graph state after Prototype 90 hardening:

| Metric | Value |
|---|---:|
| Total Concept nodes | 171 |
| Total relationships | 142 |
| LLM-generated nodes | 82 |
| LLM-generated relationships | 53 |
| Auto section nodes | 54 |
| Auto section relationships | 54 |
| Expert curated nodes imported | 35 |
| Expert curated relationships imported | 35 |
| Citation validation issues | 0 |
| Strict metadata validation | Passed |
| Unit/static tests | 16 passed |
| Retrieval eval questions | 20 |
| Retrieval Top-5 hit rate | 0.85 |
| Retrieval citation completeness | 1.0 |
| Canonical aliases applied | 3 |

Latest graph quality baseline:

| Metric | Value |
|---|---:|
| Exact duplicate name groups | 5 |
| Similar name candidates | 9 |
| Generic LLM node candidates | 10 |
| Expert-vs-LLM overlaps | 1 |
| Orphan requirements | 9 |
| Suspicious bidirectional edges | 0 |
| Citation gaps | 0 |

Generated reports:

- `Projects/ESG/graph/quality_reports/graph_quality_report.json`
- `Projects/ESG/graph/quality_reports/graph_quality_report.md`
- `Projects/ESG/graph/canonical_aliases.json`
- `Projects/ESG/graph/import_reports/canonical_aliases_apply_report.json`
- `Projects/ESG/graph/import_reports/canonical_aliases_apply_report.pre_apply.json`
- `Projects/ESG/eval/retrieval_questions.jsonl`
- `Projects/ESG/eval/retrieval_eval_report.json`
- `Projects/ESG/eval/retrieval_eval_report.md`
- `Projects/ESG/graph/citation_reports/citation_validation.latest.json`
- `Projects/ESG/manifests/run_manifest.latest.json`

Important source hashes:

- Expert `concept_map.json` source map hash:
  `fc6fada056fe91e53e05d8caa096ef6973672217fb8dfcc5fc3dd1699edc52a5`
- LLM batch 30 source map hash:
  `llm:26abb74bfc8edf654c94510119888a82ef97b9f686d4e680584e90bd32c45511`

Latest LLM batch:

| Step | Result |
|---|---:|
| Sections extracted | 30 |
| Raw LLM nodes | 147 |
| Raw LLM edges | 101 |
| Validated records retained | 29 |
| Validated nodes retained | 117 |
| Validated edges retained | 53 |

Validator behavior:

- Rejects items with evidence quotes not found in section text.
- Rejects invalid ontology labels and edge types.
- Rejects low confidence nodes/edges below default `0.5`.
- Handles safe PDF extraction artifacts such as hyphen line breaks and smart quotes.
- Performs item-level filtering: bad node/edge items are removed, while valid items in the same section can still be retained.

## 3. Architecture Decision

The project now uses a layered graph model:

```text
Markdown KB
  -> deterministic section graph
  -> validated LLM graph
  -> expert concept_map.json final enhancement/override
```

Authority order:

1. Markdown content is the evidence source.
2. Deterministic section graph is structural and low-risk.
3. LLM graph is an expansion layer, allowed only after validator filtering.
4. `concept_map.json` is expert-curated and imported last as the final enhancement layer.

There is no separate manual approval step for every LLM candidate. The expert `concept_map.json` is the final business authority.

## 4. What Has Been Hardened

Extractor:

- Fixed fragile boolean bug in heading cluster logic.
- Synchronized bold detection between extractor and debug script.
- Added source metadata emission.
- Preserves existing anchors when regenerating Markdown.
- Hashes final Markdown body after anchor preservation.

Importer:

- Flexible HTML anchor matching.
- No hardcoded KB path.
- Adds citation metadata to Neo4j nodes.
- Adds `import_batch_id` and `source_map_hash`.
- Supports stale marking/pruning.
- Imports deterministic section graph from Markdown anchors.
- Imports expert `concept_map.json` as curated overlay.

Query:

- Added bounded multi-hop graph retrieval.
- Added SQLite FTS5/BM25 local retrieval.
- Always returns citation objects.
- Compact output by default to avoid clipped CLI output.

LLM:

- Added staged OpenAI extraction.
- Added candidate validator.
- Added candidate importer.
- Added confidence threshold.
- Added item-level filtering.
- Added safe normalization for PDF line-break artifacts.

Tests:

- Added hardening tests for extractor, anchor regex, doc resolution, FTS search, citation validation, auto section graph, LLM candidate validation, and PDF hyphen line-break normalization.

## 5. Known Gaps

These are the main gaps between current state and legal-grade production.

### 5.1 Graph Canonicalization

LLM can create generic or duplicate nodes, for example:

- `ghg_emissions`
- `inventory_boundary`
- `calculation_methodologies`
- names that overlap with expert concepts or deterministic sections

Risk:

- Graph becomes noisy.
- Query paths can look plausible but semantically weak.
- Duplicate concepts split evidence across multiple nodes.

Needed:

- Alias/canonical ID mapping.
- Merge suggestions.
- Prefer expert `concept_map.json` IDs when overlap exists.
- Keep LLM provenance even after merge.

### 5.2 Relation Direction and Semantics

Some LLM relations can be bidirectional or too generic, such as `REQUIRES_ACTIVITY_DATA` around `scope_1` and `ghg_emissions`.

Risk:

- Graph paths may imply stronger legal obligations than the source supports.

Needed:

- Direction rules per edge type.
- Edge-type-specific validation.
- Stronger prompt constraints.
- Post-import relation quality checks.

### 5.3 Claim-Level Citation

Current citation points to Markdown anchor/page range. This is good, but not enough for high-stakes legal answers.

Needed:

- Evidence spans at paragraph or sentence level.
- Each generated answer claim must map to one or more evidence spans.
- Refuse or downgrade answer if a claim has no citation.

### 5.4 Retrieval Evaluation

There is no formal eval set yet.

Needed:

- 20-50 gold questions for GHG Protocol.
- Expected anchors/concepts for each question.
- Precision/recall metrics for graph, local FTS, and combined retrieval.
- Regression test command.

### 5.5 Answer Generation Guardrails

Currently retrieval is strong enough to support answers, but the system does not yet enforce answer-level legal behavior.

Needed:

- Answer script that only answers from retrieved citations.
- Mandatory citation per material claim.
- Clear "not found in KB" response.
- No unsupported extrapolation.

### 5.6 Audit Manifest

The pipeline has hashes, but not yet a single immutable manifest per run.

Needed:

- Run manifest JSON:
  - input PDFs,
  - chapter config hash,
  - concept map hash,
  - LLM model,
  - script versions,
  - output files,
  - Neo4j target,
  - validation results.

## 6. Completed Milestone: Legal-Grade Prototype 85-90%

Goal achieved:

Make the system measurable, less noisy, and safer for internal legal/compliance RAG workflows on the current GHG KB.

Completed tasks:

1. Build graph canonicalization report.
   - Detect duplicate/similar node names.
   - Detect LLM nodes overlapping expert concept IDs.
   - Detect generic nodes with too many weak relations.
   - Output JSON/Markdown report before modifying Neo4j.

2. Add canonical alias layer.
   - Create `Projects/ESG/graph/canonical_aliases.json`.
   - Map LLM IDs to expert IDs where appropriate.
   - Importer should merge or redirect LLM nodes based on alias map.

3. Add retrieval eval set.
   - Create `Projects/ESG/eval/retrieval_questions.jsonl`.
   - Start with 20 questions:
     - scope 1 definition,
     - scope 2 definition,
     - scope 3 optionality,
     - reporting requirements,
     - base year recalculation,
     - organizational boundary,
     - equity share vs control,
     - biomass CO2 treatment,
     - verification,
     - target base year.

4. Add eval runner.
   - Run query for each question.
   - Check whether expected anchor/concept appears in top K.
   - Report hit rate and missing cases.

5. Add answer generator prototype.
   - Input: user question.
   - Retrieve graph + local text.
   - Compose answer only from cited evidence.
   - Refuse when evidence is insufficient.

Acceptance status:

- Citation validation has `issue_count: 0`.
- Tests pass: `16 passed`.
- Retrieval eval has 20 questions.
- Top-5 retrieval hit rate is `0.85`.
- `scope_1`, `scope_2`, `scope_3`, `reporting_required`, and `base_year_selection` return complete citations.
- Answer generator returns only cited claims and refuses unsupported token cases.
- Run manifest exists at `Projects/ESG/manifests/run_manifest.latest.json`.

## 7. Next Milestone: Legal-Grade Prototype 80-85%

Target duration: 3-5 focused days.

Tasks:

1. Expand eval set to 50-100 questions.
2. Add query expansion for legal/compliance terms.
3. Add vector retrieval or reranking.
4. Add paragraph/sentence evidence index.
5. Add answer-level citation checker.
6. Add run manifest.
7. Add sync/change detection for changed Markdown files.
8. Add graph quality dashboard/report:
   - orphan requirements,
   - weak edges,
   - duplicate nodes,
   - stale nodes,
   - citation gaps.

Acceptance criteria:

- Top-5 retrieval hit rate target: 80%+ on internal eval set.
- Zero citation validation issues.
- Every answer includes citations.
- System refuses unsupported questions.
- Rerun pipeline is reproducible from manifest.

## 8. Production Legal-Grade Direction

Target duration: several weeks, depending on number and complexity of source documents.

Tasks:

1. PDF paragraph/page/bbox mapping.
2. Multi-document source conflict handling.
3. Domain expert eval review.
4. Formal change log and signed run manifests.
5. Versioned KB releases.
6. Permission-aware retrieval if sources have restricted access.
7. Monitoring:
   - failed retrieval,
   - low-confidence answers,
   - citation drift,
   - graph growth/noise.

Production definition:

- A domain expert can audit every material claim back to exact evidence.
- The system can say "not found" instead of guessing.
- Changes in source documents produce traceable changes in graph and retrieval behavior.
- Regression eval prevents silent quality degradation.

## 9. Recommended Immediate Next Step

Start with canonicalization and eval.

Completed baseline work item:

```text
Build scripts/analyze_graph_quality.py
```

It now produces:

- duplicate node candidates,
- generic LLM node candidates,
- expert-vs-LLM overlaps,
- orphan requirements,
- edge direction anomalies,
- citation completeness summary.

Completed next work item:

```text
Create Projects/ESG/graph/canonical_aliases.json and apply it in the LLM importer/query layer.
```

Current conservative aliases:

- `control_approach` -> `boundary_control`
- `equity_share_approach` -> `boundary_equity_share`
- `requirement_accuracy` -> `accuracy`

Implemented support:

- `import_llm_candidates.py --aliases Projects/ESG/graph/canonical_aliases.json`
- `import_llm_candidates.py --dry-run`
- `scripts/apply_canonical_aliases.py` with dry-run default and destructive merge only behind `--apply`

Alias apply result:

- Alias count: 3
- Applied aliases: 3
- Migrated relationships: 4
- Removed alias source nodes: 3

The deferred aliases remain unapplied. Do not apply them until their ontology role is reviewed.

The first retrieval eval set has been created and baseline measured. Do not add more LLM extraction until remaining generic LLM nodes and orphan requirements are reviewed.

Reason:

The graph is now large enough to be useful, but also large enough to accumulate noise. More extraction before quality analysis will increase cleanup cost.
