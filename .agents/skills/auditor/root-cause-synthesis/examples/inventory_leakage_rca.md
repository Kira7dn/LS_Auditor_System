# Example: Root Cause Synthesis (Inventory Leakage)

## 1. Observed Exceptions (Symptoms)
- **EXC-01**: 15% of raw materials have >120 days of stock (Threshold is 60).
- **EXC-02**: Multiple POs for "Material X" were issued while 500 units were still in the warehouse.
- **EXC-03**: Scrap rate for "Material X" is reported at 2%, but actual waste measured is 7%.

## 2. Synthesis (Pattern Recognition)
These exceptions point to a **Systemic Failure in the Planning-Production Feedback Loop**.
The Planning department is using static BOM multipliers that do not account for actual inventory levels or real-world scrap rates.

## 3. Root Cause (The "Why")
- **Primary Root Cause**: Lack of real-time integration between the Inventory Management System and the MRP (Material Requirements Planning) module.
- **Secondary Root Cause**: Manual entry of scrap rates based on "historical estimates" rather than actual production data.

## 4. Impact Assessment
- **Financial Leakage**: $45,000 in tied-up capital + $12,000 in material waste annually.
- **Risk Level**: High (Direct impact on Gross Margin).
