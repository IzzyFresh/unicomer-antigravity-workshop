import pytest
from fastapi.testclient import TestClient
from main import app, calculate_dti_ratio, get_base_interest_rate

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_calculate_dti_ratio():
    # Monthly income: 1000, Debt: 200, Installment: 100 -> DTI = 300 / 1000 = 0.30
    dti = calculate_dti_ratio(monthly_income=1000.0, monthly_debt=200.0, requested_installment=100.0)
    assert dti == 0.30

def test_credit_evaluation_approved():
    payload = {
        "customer_id": "DUI-01234567-8",
        "customer_name": "Juan Perez",
        "phone_number": "+50370001122",
        "brand": "LA_CURACAO",
        "monthly_income": 1200.0,
        "monthly_debt_obligations": 150.0,
        "requested_amount": 500.0,
        "term_months": 12,
        "tier": "STANDARD"
    }
    response = client.post("/api/v1/credit/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is True
    assert data["max_approved_amount"] == 500.0
    assert data["calculated_dti"] <= 0.40

def test_credit_evaluation_high_dti_counter_offer():
    payload = {
        "customer_id": "DUI-98765432-1",
        "customer_name": "Maria Lopez",
        "phone_number": "+50378889900",
        "brand": "GOLLO",
        "monthly_income": 600.0,
        "monthly_debt_obligations": 230.0,
        "requested_amount": 1500.0,
        "term_months": 12,
        "tier": "STANDARD"
    }
    response = client.post("/api/v1/credit/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is False
    assert "Rejected requested amount" in data["decision_reason"]
    assert data["max_approved_amount"] > 0
