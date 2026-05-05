# Example: Price Variance Analysis Report

## Audit Scope
- **Category**: Raw Fabric (Polyester)
- **Period**: Q1 2026
- **Objective**: Identify price leakage vs. market benchmarks.

## Findings Summary

| Material ID | Avg Purchase Price | Market Benchmark | Variance (%) | Estimated Leakage |
|-------------|--------------------|------------------|--------------|-------------------|
| FAB-POL-01  | $4.50 / yd         | $3.80 / yd       | +18.4%       | $14,000           |
| FAB-POL-05  | $4.20 / yd         | $3.90 / yd       | +7.7%        | $3,200            |
| **Total**   |                    |                  |              | **$17,200**       |

## Analysis & Root Cause Hypothesis

1. **Spot Buying**: FAB-POL-01 was purchased in small batches from secondary distributors instead of the primary supplier, leading to an 18% premium.
2. **Emergency Orders**: PO #99283 was issued with a 2-day lead time, incurring a "rush fee" hidden in the unit price.

## Recommended Action
- Consolidate Q2 demand into a single Master Purchase Agreement (MPA) with Supplier X to lock in the $3.80 rate.
