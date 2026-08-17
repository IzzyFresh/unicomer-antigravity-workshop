---
name: unicomer-api-standards
description: Enforces Grupo Unicomer enterprise REST API design standards, OpenAPI documentation, and error envelope formats.
---

# Unicomer Enterprise API Standards Skill

Use this skill whenever designing, modifying, or reviewing RESTful APIs across Unicomer projects.

## 1. URL Path Structure
- All endpoints must include semantic versioning in the path: `/api/v1/...`
- Use kebab-case for resource paths: e.g., `/api/v1/credit-evaluations`, `/api/v1/loyalty-points`.
- Mandatory `/health` and `/ready` endpoints under root for Kubernetes/Cloud Run health probes.

## 2. Standardized Error Response Envelope
All HTTP 4xx and 5xx errors must return the standard JSON envelope:
```json
{
  "error": {
    "code": "INVALID_DTI_EXCEEDED",
    "message": "Human readable error description",
    "timestamp": "2026-08-17T12:00:00Z",
    "tracking_id": "req-uuid-v4"
  }
}
```

## 3. OpenAPI Documentation
- Every endpoint must specify explicit `summary`, `description`, `response_model`, and `tags`.
- Every request payload field must include Pydantic `Field(..., description="...")` with validation constraints.
