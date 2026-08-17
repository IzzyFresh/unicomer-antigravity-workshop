---
name: pytest-mock-generator
description: Generates comprehensive Pytest test suites with fixtures, mock clients (respx, unittest.mock, httpx), parameterized edge cases, and 90%+ branch coverage.
---

# Pytest Mock & Test Suite Generator Skill

Use this skill whenever writing, expanding, or auditing automated test suites for Python backend applications.

## 1. Test Suite Structure
Organize tests by layer and purpose:
```
tests/
├── conftest.py              # Shared fixtures (TestClient, DB sessions, mock tokens)
├── unit/                    # Fast isolated unit tests for Service & Domain logic
│   └── test_services.py
└── integration/             # Integration tests for FastAPI endpoints with mock clients
    └── test_endpoints.py
```

## 2. Mandatory Testing Standards

1. **FastAPI TestClient Fixture:**
   ```python
   import pytest
   from fastapi.testclient import TestClient
   from main import app

   @pytest.fixture
   def client():
       with TestClient(app) as c:
           yield c
   ```

2. **Parameterized Edge Cases (`@pytest.mark.parametrize`):**
   - Always test boundaries: `0`, negative numbers, max integer, empty strings, malformed UUIDs, unexpected types.
   - Example:
     ```python
     @pytest.mark.parametrize("income,debt,expected_status", [
         (0.0, 100.0, 422),        # Invalid zero income (validation error)
         (-500.0, 100.0, 422),     # Negative income
         (5000.0, 0.0, 200),       # Zero debt (happy path)
         (1000.0, 900.0, 200),     # High DTI scenario
     ])
     def test_boundary_inputs(client, income, debt, expected_status):
         ...
     ```

3. **External Service Mocking:**
   - NEVER make live external HTTP calls in unit tests.
   - Use `unittest.mock.patch` or `respx` to mock external API responses and exceptions.

4. **Coverage Target:**
   - Target >= 90% branch coverage for all core service layers.
