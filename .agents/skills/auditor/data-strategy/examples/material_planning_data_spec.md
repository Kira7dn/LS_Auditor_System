# Example: Material Planning Data Strategy

This example demonstrates how to design an audit-ready data schema for a material planning audit.

## 1. Source Data Inventory

| Source System | Table Name | Key Fields | Purpose |
|---------------|------------|------------|---------|
| ERP - Production | `BOM_Master` | `Material_ID`, `Parent_ID`, `Qty_Per` | Define required quantity |
| ERP - Inventory | `Stock_Balance` | `Material_ID`, `Warehouse_ID`, `Qty_On_Hand` | Current stock levels |
| ERP - Procurement| `PO_Lines` | `PO_Number`, `Material_ID`, `Order_Qty`, `Unit_Price` | Actual purchase data |
| Excel - Planning | `Monthly_Forecast`| `Material_ID`, `Month`, `Forecast_Qty` | Target production demand |

## 2. Join Logic

To identify leakage, we need to join these tables into a `Unified_Audit_Dataset`:

```sql
SELECT 
    f.Material_ID,
    f.Forecast_Qty,
    (f.Forecast_Qty * b.Qty_Per) AS Calculated_Demand,
    s.Qty_On_Hand,
    p.Order_Qty,
    p.Unit_Price,
    ((p.Order_Qty + s.Qty_On_Hand) - (f.Forecast_Qty * b.Qty_Per)) AS Excess_Supply
FROM Monthly_Forecast f
JOIN BOM_Master b ON f.Material_ID = b.Parent_ID
LEFT JOIN Stock_Balance s ON b.Material_ID = s.Material_ID
LEFT JOIN PO_Lines p ON b.Material_ID = p.Material_ID
```

## 3. Normalization Rules

- **UoM (Unit of Measure)**: All quantities must be converted to the base BOM unit (e.g., Yards for fabric, Kg for chemicals).
- **Currency**: Convert all `Unit_Price` to USD using the monthly average exchange rate.
- **Timestamp**: Align all records to the `Production_Month` for trend analysis.

## 4. Expected Audit Artifacts

- **Data Quality Log**: Documenting missing BOM records or orphaned POs.
- **Unified Dataset**: A Parquet file containing the joined and cleaned data for `variance-analysis`.
