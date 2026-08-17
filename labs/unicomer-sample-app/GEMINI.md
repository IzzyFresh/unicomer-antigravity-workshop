# Unicomer Retail Credit Microservice - Antigravity Rules

## Architecture & Code Guidelines
1. **Framework:** FastAPI with Pydantic v2 schemas and strict typing.
2. **Financial Precision:** All financial calculations (installments, interest, DTI) must round to 2 or 4 decimal places explicitly.
3. **Security & Privacy:** NEVER log customer PII (DUI, NIT, Cedula, mobile numbers) in plaintext. Always mask sensitive identifiers.
4. **Testing:** Every endpoint modification requires corresponding `pytest` test cases in `test_main.py`.
5. **Skills Compliance:** Always reference `.agents/skills/` for domain rules (e.g. `unicomer-credit-policy` and `unicomer-api-standards`).
