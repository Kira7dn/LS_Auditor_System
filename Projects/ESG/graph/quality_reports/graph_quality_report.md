# Graph Quality Report

Generated at: 2026-06-14T03:57:10Z

## Summary

| Metric | Value |
|---|---:|
| `node_count` | 171 |
| `relationship_count` | 142 |
| `llm_node_count` | 82 |
| `auto_node_count` | 54 |
| `llm_relationship_count` | 53 |
| `auto_relationship_count` | 54 |
| `citation_gap_count` | 0 |
| `exact_duplicate_name_group_count` | 5 |
| `similar_name_candidate_count` | 9 |
| `generic_llm_node_count` | 10 |
| `expert_llm_overlap_count` | 1 |
| `orphan_requirement_count` | 9 |
| `bidirectional_edge_count` | 0 |
| `low_confidence_edge_count` | 0 |

## Exact Duplicate Names

- `accuracy` (2 nodes): `accuracy`, `principles_accuracy`
- `completeness` (2 nodes): `completeness`, `principles_completeness`
- `consistency` (2 nodes): `consistency`, `principles_consistency`
- `relevance` (2 nodes): `principles_relevance`, `relevance`
- `transparency` (2 nodes): `principles_transparency`, `transparency`

## Similar Name Candidates

- score `0.952`: `direct_ghg_emissions` (Direct GHG emissions) <-> `indirect_ghg_emissions` (Indirect GHG emissions)
- score `0.951`: `verification` (Verification of GHG Emissions) <-> `verification_process` (10 Verification of GHG Emissions)
- score `0.901`: `calc_steps` (Steps in identifying and calculating GHG emissions) <-> `identifying_calculating` (Identifying and Calculating GHG Emissions)
- score `0.889`: `chapter_3` (Chapter 3) <-> `chapter_7` (Chapter 7)
- score `0.889`: `chapter_3` (Chapter 3) <-> `chapter_9` (Chapter 9)
- score `0.889`: `chapter_7` (Chapter 7) <-> `chapter_9` (Chapter 9)
- score `0.889`: `oper_boundaries` (Setting Operational Boundaries) <-> `org_boundaries` (Setting Organizational Boundaries)
- score `0.875`: `emissions_recalculation` (Emissions Recalculation) <-> `ghg_emissions` (GHG emissions calculation)
- score `0.862`: `org_boundaries` (Setting Organizational Boundaries) <-> `organizational_boundaries` (Organizational boundaries)

## Generic LLM Nodes

- `ghg_emissions` (GHG emissions calculation), label `Requirement`, degree `5`
- `financial_control` (Financial Control), label `ControlType`, degree `4`
- `inventory_boundary` (Inventory boundary), label `BoundaryRule`, degree `4`
- `company_control` (Company Control), label `Company`, degree `3`
- `operational_control` (Operational Control), label `ControlType`, degree `3`
- `bp_equity_share` (BP), label `Company`, degree `2`
- `company` (A company), label `Company`, degree `2`
- `economic_substance` (Economic substance), label `Principle`, degree `2`
- `finding_emission_sources` (Emission Sources), label `Finding`, degree `2`
- `scopes_definition` (Scopes Definition), label `Definition`, degree `2`

## Expert vs LLM Overlaps

- score `0.862`: LLM `organizational_boundaries` (Organizational boundaries) -> expert `org_boundaries` (Setting Organizational Boundaries)

## Orphan Requirements

- `company_responsibility` (Company Responsibility), llm_generated=`True`
- `direct_ghg_emissions` (Direct GHG emissions), llm_generated=`True`
- `emission_factor_changes` (Changes in emission factor), llm_generated=`True`
- `ghg_targets` (GHG Targets), llm_generated=`True`
- `indirect_ghg_emissions` (Indirect GHG emissions), llm_generated=`True`
- `outsourcing_insourcing_emissions_tracking` (Tracking emissions for outsourcing/insourcing), llm_generated=`True`
- `recalculation_timing` (Recalculation Timing), llm_generated=`True`
- `significant_change` (Significant Change), llm_generated=`True`
- `verifier_responsibility` (Verifier Responsibility), llm_generated=`True`

## Suspicious Bidirectional Edges

No issues found.

## Citation Gaps

No issues found.

## Top Degree Nodes

- `identifying_calculating` (Identifying and Calculating GHG Emissions), degree `8`, in `0`, out `8`, llm=`False`
- `tracking_time` (Tracking Emissions Over Time), degree `8`, in `0`, out `8`, llm=`False`
- `ghg_protocol` (GHG Protocol Corporate Standard (Revised Edition)), degree `7`, in `0`, out `7`, llm=`False`
- `targets` (Setting a GHG Target), degree `7`, in `0`, out `7`, llm=`False`
- `accuracy` (Accuracy), degree `6`, in `5`, out `1`, llm=`False`
- `emission_factor_method` (Emission Factor Calculation Approach), degree `6`, in `0`, out `6`, llm=`False`
- `org_boundaries` (Setting Organizational Boundaries), degree `6`, in `0`, out `6`, llm=`False`
- `req_scope_reporting` (Companies shall separately account for and report scopes 1 and 2 at a minimum), degree `6`, in `5`, out `1`, llm=`False`
- `boundary_completeness_check` (Verify completeness of corporate boundary and consolidation approach), degree `5`, in `1`, out `4`, llm=`False`
- `contracts_ghg_emissions` (Contracts that cover GHG emissions), degree `5`, in `1`, out `4`, llm=`False`
- `ghg_emissions` (GHG emissions calculation), degree `5`, in `4`, out `1`, llm=`True`
- `oper_boundaries` (Setting Operational Boundaries), degree `5`, in `0`, out `5`, llm=`False`
- `principles` (GHG Accounting and Reporting Principles), degree `5`, in `0`, out `5`, llm=`False`
- `base_year_selection` (Choosing a base year), degree `4`, in `1`, out `3`, llm=`False`
- `consistency` (Consistency), degree `4`, in `4`, out `0`, llm=`False`
- `financial_control` (Financial Control), degree `4`, in `3`, out `1`, llm=`True`
- `inventory_boundary` (Inventory boundary), degree `4`, in `3`, out `1`, llm=`True`
- `recalc_significance` (Articulate base year recalculation policy and significance threshold), degree `4`, in `3`, out `1`, llm=`False`
- `reporting` (Reporting GHG Emissions), degree `4`, in `0`, out `4`, llm=`False`
- `scope_2` (Scope 2: Electricity indirect GHG emissions), degree `4`, in `1`, out `3`, llm=`False`

## Recommended Next Actions

1. Review `expert_llm_overlaps` and create `Projects/ESG/graph/canonical_aliases.json` for safe merges.
2. Inspect `generic_llm_nodes` before running more LLM extraction.
3. Resolve suspicious bidirectional edges by edge-type direction rules.
4. Keep `citation_gap_count` at `0` before using the graph for legal-grade answers.
