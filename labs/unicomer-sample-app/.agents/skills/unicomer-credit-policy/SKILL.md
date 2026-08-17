---
name: unicomer-credit-policy
description: Applies Unicomer retail credit policies, DTI constraints, and brand-specific financing rules for El Salvador and LATAM (La Curacao, Gollo, RadioShack, Emma).
---

# Unicomer Retail Credit Policy Skill

When evaluating, generating, or refactoring credit and financing code for Grupo Unicomer retail systems, strictly enforce the following business rules and constraints:

## 1. Debt-to-Income (DTI) Ceilings
- **Standard Customers (STANDARD / SILVER):** Maximum allowable DTI ratio is **40.0%** (0.40).
- **VIP Customers (GOLD / PLATINUM):** Maximum allowable DTI ratio is **45.0%** (0.45).
- **Calculation Formula:**
  $$\text{DTI} = \frac{\text{Monthly Debt Obligations} + \text{New Requested Installment}}{\text{Verifiable Monthly Income}}$$

## 2. Financing Caps by Brand
- **LA_CURACAO:** Maximum financing amount without manual credit committee review is **$3,500 USD**.
- **GOLLO:** Maximum automated financing amount is **$2,500 USD**.
- **EMMA (Digital Fintech):** Maximum automated financing amount is **$1,500 USD**.
- **RADIOSHACK:** Maximum automated financing amount is **$1,000 USD**.

## 3. PII & Financial Data Protection (Regulatory Compliance)
- **NEVER** print plain text Document IDs (DUI, NIT, Cedula) or customer mobile phone numbers to application logs or error traces.
- Mask identifiers in logs: e.g., `DUI-***4567-8` or hash the identifier before logging.

## 4. Response Standardization
All credit evaluation responses must provide:
- `approved`: boolean
- `max_approved_amount`: float
- `calculated_dti`: float formatted to 4 decimals
- `interest_rate_annual`: float
- `monthly_installment`: float
- `decision_reason`: clear Spanish or English explanation detailing approval basis or counter-offer logic.
