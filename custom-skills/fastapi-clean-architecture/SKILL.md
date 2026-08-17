---
name: fastapi-clean-architecture
description: Enforces Clean/Hexagonal Architecture for Python FastAPI services, separating Routers, Service layer, Repositories, and Pydantic v2 schemas.
---

# FastAPI Clean Architecture Skill

Use this skill whenever scaffolding, refactoring, or reviewing Python backend services with FastAPI.

## 1. Architectural Layers & Separation of Concerns

Every new feature or entity must be organized into four distinct layers:

```
[ Routers / Endpoints (FastAPI) ]
             ↓ (Depends)
[ Service Layer (Business Logic) ]
             ↓
[ Repository / Data Layer (Async DB/Client) ]
             ↓
[ Domain Models & Pydantic v2 Schemas ]
```

### Layer Rules:
1. **Routers (`routers/`):**
   - Handle HTTP requests, query/path parameters, and status codes.
   - **No direct database queries or raw business logic.**
   - Inject services using FastAPI `Depends()`.
2. **Service Layer (`services/`):**
   - Pure Python business logic, validations, and workflow orchestration.
   - Return clean domain objects or raise typed domain exceptions.
3. **Repository Layer (`repositories/`):**
   - Abstract database and external API interactions.
   - Use asynchronous non-blocking patterns (`async`/`await`).
4. **Schemas (`schemas/`):**
   - Use Pydantic v2 `BaseModel` with strict type annotations and field descriptions.

## 2. Standardized Error Handling
Raise custom domain exceptions in the service layer, handled by FastAPI exception handlers that return standard error envelopes:
```python
from fastapi import HTTPException, status

class EntityNotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
```

## 3. Asynchronous Execution
- Every I/O operation (HTTP calls, DB queries, file reads) must be asynchronous (`async def`).
- CPU-bound operations must not block the main asyncio event loop.
