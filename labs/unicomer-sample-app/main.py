"""
Unicomer Retail Credit & Loyalty Eligibility Microservice
Target Brands: La Curacao, Gollo, RadioShack, Emma
"""

import logging
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("unicomer-credit-service")

app = FastAPI(
    title="Unicomer Credit Eligibility & Loyalty API",
    description="Microservice to evaluate retail customer credit applications and calculate loyalty rewards across LATAM brands.",
    version="1.0.0"
)

# ---------------------------------------------------------
# Request / Response Schemas
# ---------------------------------------------------------
class CreditEvaluationRequest(BaseModel):
    customer_id: str = Field(..., description="Unique customer identifier (e.g. DUI / NIT / Cedula)")
    customer_name: str = Field(..., description="Full legal customer name")
    phone_number: str = Field(..., description="Customer mobile number")
    brand: str = Field(..., description="Retail brand: 'LA_CURACAO', 'GOLLO', 'RADIOSHACK', 'EMMA'")
    monthly_income: float = Field(..., gt=0, description="Verifiable monthly income in USD")
    monthly_debt_obligations: float = Field(..., ge=0, description="Existing monthly debt payments in USD")
    requested_amount: float = Field(..., gt=0, description="Amount requested for financing in USD")
    term_months: int = Field(..., gt=0, le=60, description="Repayment term in months (12, 24, 36, 48, 60)")
    tier: str = Field(default="STANDARD", description="Loyalty tier: 'STANDARD', 'SILVER', 'GOLD', 'PLATINUM'")


class CreditEvaluationResponse(BaseModel):
    customer_id: str
    approved: bool
    max_approved_amount: float
    calculated_dti: float
    interest_rate_annual: float
    monthly_installment: float
    decision_reason: str
    loyalty_bonus_points: int


class LoyaltyPointsRequest(BaseModel):
    customer_id: str
    tier: str
    purchase_amount: float


class LoyaltyPointsResponse(BaseModel):
    customer_id: str
    points_earned: int
    multiplier_applied: float


# ---------------------------------------------------------
# Business Logic Helpers
# ---------------------------------------------------------
def calculate_dti_ratio(monthly_income: float, monthly_debt: float, requested_installment: float) -> float:
    """
    Calculate Debt-to-Income (DTI) ratio.
    Target formula: (monthly_debt + requested_installment) / monthly_income
    """
    total_monthly_obligations = monthly_debt + requested_installment
    # Intentional edge-case: If income is 0 or negative (guarded by Pydantic, but internally needs precision)
    if monthly_income <= 0:
        return 1.0
    return round(total_monthly_obligations / monthly_income, 4)


def get_base_interest_rate(brand: str, tier: str) -> float:
    """
    Determine annual interest rate based on brand & tier.
    """
    base_rate = 0.24  # Default 24% annual
    
    brand_discounts = {
        "LA_CURACAO": 0.02,
        "GOLLO": 0.02,
        "EMMA": 0.04,
        "RADIOSHACK": 0.01,
    }
    tier_discounts = {
        "STANDARD": 0.00,
        "SILVER": 0.02,
        "GOLD": 0.04,
        "PLATINUM": 0.06,
    }
    
    rate = base_rate - brand_discounts.get(brand.upper(), 0.0) - tier_discounts.get(tier.upper(), 0.0)
    return max(rate, 0.10)  # Floor at 10%


# ---------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------
@app.get("/health", tags=["System"])
def health_check():
    return {"status": "healthy", "service": "unicomer-credit-service"}


@app.post("/api/v1/credit/evaluate", response_model=CreditEvaluationResponse, tags=["Credit"])
def evaluate_credit(request: CreditEvaluationRequest):
    # SECURITY ISSUE (FOR LAB): Logging sensitive PII data in plaintext
    logger.info(f"Evaluating credit for customer_id={request.customer_id}, name={request.customer_name}, phone={request.phone_number}")

    interest_rate = get_base_interest_rate(request.brand, request.tier)
    monthly_interest = interest_rate / 12.0
    
    # Calculate simple installment (Principal + monthly interest amortized)
    # Simple installment approximation
    estimated_monthly_installment = (request.requested_amount / request.term_months) * (1 + monthly_interest)

    dti = calculate_dti_ratio(request.monthly_income, request.monthly_debt_obligations, estimated_monthly_installment)

    # Business Rule: Unicomer Max DTI threshold is 0.40 (40%)
    max_dti_threshold = 0.40
    if request.tier in ["GOLD", "PLATINUM"]:
        max_dti_threshold = 0.45

    approved = False
    max_approved_amount = 0.0
    decision_reason = ""

    if dti <= max_dti_threshold:
        approved = True
        max_approved_amount = request.requested_amount
        decision_reason = f"Approved: DTI {dti:.2%} is within acceptable limit of {max_dti_threshold:.2%}."
    else:
        approved = False
        # Calculate maximum possible loan amount under threshold
        max_allowable_installment = (request.monthly_income * max_dti_threshold) - request.monthly_debt_obligations
        if max_allowable_installment > 0:
            max_approved_amount = round((max_allowable_installment / (1 + monthly_interest)) * request.term_months, 2)
            decision_reason = f"Rejected requested amount due to high DTI ({dti:.2%}). Counter-offer maximum eligible amount calculated."
        else:
            max_approved_amount = 0.0
            decision_reason = f"Rejected: Existing debt obligations exceed max DTI threshold of {max_dti_threshold:.2%}."

    # Calculate loyalty bonus
    loyalty_bonus = 0
    if approved:
        loyalty_bonus = int(request.requested_amount * 0.10)

    return CreditEvaluationResponse(
        customer_id=request.customer_id,
        approved=approved,
        max_approved_amount=max_approved_amount,
        calculated_dti=dti,
        interest_rate_annual=interest_rate,
        monthly_installment=round(estimated_monthly_installment, 2),
        decision_reason=decision_reason,
        loyalty_bonus_points=loyalty_bonus
    )


@app.post("/api/v1/loyalty/calculate-points", response_model=LoyaltyPointsResponse, tags=["Loyalty"])
def calculate_loyalty(request: LoyaltyPointsRequest):
    multipliers = {
        "STANDARD": 1.0,
        "SILVER": 1.5,
        "GOLD": 2.0,
        "PLATINUM": 3.0
    }
    multiplier = multipliers.get(request.tier.upper(), 1.0)
    points = int(request.purchase_amount * multiplier)
    
    return LoyaltyPointsResponse(
        customer_id=request.customer_id,
        points_earned=points,
        multiplier_applied=multiplier
    )
