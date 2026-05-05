# Example: Evidence Pack (Unauthorized Price Change)

## Finding ID: FIND-2026-004
**Summary**: Unauthorized unit price increase for Vendor "Z" without Procurement Manager approval.

## Evidence Items

### 1. Transaction Data Link
- **PO Number**: [PO-88273](file:///data/raw/procurement/po_q1.csv#L452)
- **Material**: Chemical-X1
- **Recorded Price**: $12.50 / kg
- **Contract Price**: $10.00 / kg
- **Leakage Value**: $2,500 (Qty: 1,000 kg)

### 2. System Logs
- **Timestamp**: 2026-02-15 14:30:05
- **User ID**: `purch_assistant_02`
- **Action**: Unit Price Override
- **Approval Flag**: `FALSE`

### 3. Visual Proof
![Price Override Screenshot](file:///assets/evidence/PO-88273_override.png)
*Caption: ERP interface showing the manual price override without mandatory approval field populated.*

## Verification Status
- [x] Transaction ID Verified
- [x] Financial Impact Calculated
- [x] Responsible Party Identified
- [ ] Stakeholder Confirmed
