# Retrieval Eval Report

| Metric | Value |
|---|---:|
| `question_count` | 20 |
| `successful_query_count` | 20 |
| `top_1_hit_rate` | 0.45 |
| `top_5_hit_rate` | 0.85 |
| `anchor_hit_rate` | 0.8 |
| `concept_hit_rate` | 0.6 |
| `citation_complete_rate` | 1.0 |

## Cases

- `PASS` `scope_1_definition`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `scope_2_definition`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `scope_3_definition`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `FAIL` `scope_reporting_minimum`: top5=`False`, anchor=`False`, concept=`False`, citations=`5`
- `PASS` `biomass_co2_scope1`: top5=`True`, anchor=`True`, concept=`False`, citations=`1`
- `PASS` `kyoto_gases_scope1`: top5=`True`, anchor=`True`, concept=`False`, citations=`5`
- `PASS` `organizational_boundary`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `control_approach`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `equity_share_approach`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `base_year_selection`: top5=`True`, anchor=`True`, concept=`False`, citations=`1`
- `FAIL` `recalculation_rules`: top5=`False`, anchor=`False`, concept=`False`, citations=`3`
- `PASS` `significance_threshold`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `structural_changes`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
- `PASS` `calculation_steps`: top5=`True`, anchor=`True`, concept=`True`, citations=`2`
- `PASS` `identify_sources`: top5=`True`, anchor=`True`, concept=`False`, citations=`4`
- `FAIL` `emission_factor_selection`: top5=`False`, anchor=`False`, concept=`False`, citations=`3`
- `PASS` `inventory_quality`: top5=`True`, anchor=`False`, concept=`True`, citations=`2`
- `PASS` `reporting_required`: top5=`True`, anchor=`True`, concept=`False`, citations=`4`
- `PASS` `verification_process`: top5=`True`, anchor=`True`, concept=`True`, citations=`2`
- `PASS` `target_base_year`: top5=`True`, anchor=`True`, concept=`True`, citations=`5`
