# 🎙️ Live Demo Cheat Sheet: Antigravity 2.0 & Engineering Skills (Unicomer)

**Target Audience:** Alejandro, Mauricio & Unicomer Engineering Leads (Users of Claude Code & modern IDEs)  
**Presenter:** Israel Castillo  
**Core Storyline:** Demonstrating the ease of **creating, extracting, and executing pure Software Engineering Skills in Antigravity 2.0 via natural language prompts**, orchestrating parallel subagents, and comparing with Claude Code.

---

## ⏱️ Live Demo Timeline (12 - 15 Minutes Total)

```
[00:00 - 02:00] Act 1: Set the Stage & Implementation Plan in Antigravity 2.0
[02:00 - 05:00] Act 2: Prompt-Driven Coding Skills Creation (Clean Architecture & Pytest Mocks)
[05:00 - 09:00] Act 3: Launch Parallel Subagents (Architecture Refactor, Security, QA)
[09:00 - 11:00] Act 4: Sandbox Verification & Inspectable Walkthrough Artifact
[11:00 - 14:00] Act 5: The Claude Code vs. Antigravity 2.0 Direct Comparison
[14:00 - 15:00] Q&A & Developer Hands-on Kickoff
```

---

## 🎬 Act 1: Set the Stage & Implementation Plan

### 🗣️ Speaker Intro:
> *"Today, let's explore Antigravity 2.0. Instead of treating AI as just a chat window or line-autocompleter, we'll give it high-level engineering objectives for our Unicomer Retail Credit Microservice."*

### 📋 Prompt 1 (Plan):
```text
Analyze this repository. We need to refactor our monolithic main.py into a modular, production-ready service:
1. Break down main.py using Clean Architecture (Routers, Services, Repositories, Schemas).
2. Ensure non-blocking async execution for all endpoint handlers.
3. Fix the critical PII logging issue where customer identification and phone numbers are exposed in plaintext.

Please generate an Implementation Plan detailing the proposed file structure, testing strategy, and risk assessment. Do not modify code yet.
```

---

## ⚡ Act 2: Creating Software Engineering Skills Live via Prompts in Antigravity 2.0

### 🗣️ Speaker Talking Point:
> *"How do you standardize architecture and testing across all Unicomer development squads? In Antigravity 2.0, you create reusable coding skills in seconds with natural language prompts."*

### 📋 Prompt 2A (Create Clean Architecture Coding Skill):
```text
Create a new engineering skill in .agents/skills/fastapi-clean-architecture/SKILL.md that enforces Clean/Hexagonal Architecture for Python backend services:
- Strict layer separation: Routers (Depends injection) -> Services (Pure domain logic & typed exceptions) -> Repositories (Async data access) -> Schemas (Pydantic v2).
- Routers must never execute direct database queries or heavy calculations.
- All I/O functions must be async def.
- Standard HTTP exception handling.
Include YAML frontmatter, rules, and code templates.
```

### 📋 Prompt 2B (Create Automated Pytest & Mock Generator Skill):
```text
Create a developer testing skill in .agents/skills/pytest-mock-generator/SKILL.md instructing the agent to:
- Generate reusable conftest.py fixtures using FastAPI TestClient.
- Write parameterized test suites with @pytest.mark.parametrize to test boundary conditions (zero, negative numbers, extreme values).
- Mock external dependencies with unittest.mock or respx.
- Target >= 90% branch coverage.
```

---

## 🤖 Act 3: Spawning Parallel Subagents in Antigravity 2.0

### 🗣️ Speaker Talking Point:
> *"Now our Lead Agent orchestrates 3 specialized subagents running concurrently to execute the refactoring and test generation."*

### 📋 Prompt 3:
```text
Execute our implementation plan and apply our new 'fastapi-clean-architecture' and 'pytest-mock-generator' skills using 3 specialized subagents in parallel:
- Subagent 1 (Role: 'Backend Architect'): Refactor main.py into routers/, services/, and schemas/ following our clean architecture skill.
- Subagent 2 (Role: 'Security & Compliance Auditor'): Sanitize and mask all customer PII (DUI/NIT and phone) in logs across all service layers.
- Subagent 3 (Role: 'QA Test Automation Engineer'): Generate comprehensive unit tests in tests/ with parameterized fixtures following our pytest skill.

Coordinate and report back when all subagents complete their work.
```

---

## 🛡️ Act 4: Sandbox Verification & Walkthrough Artifact

### 🗣️ Speaker Talking Point:
> *"Antigravity verifies its own work inside a secure execution sandbox before handing it back to the developer."*

### 📋 Prompt 4:
```text
Execute pytest on the test suite in the sandbox to verify that 100% of tests pass. Then generate a comprehensive walkthrough.md artifact summarizing all changes, architectural layers created, and test coverage metrics.
```

---

## 🥊 Act 5: Claude Code vs. Antigravity 2.0 Comparison for Developers

### Talking points for teams familiar with Claude Code:

| Capability | Claude Code | Google Antigravity 2.0 |
| :--- | :--- | :--- |
| **Engineering Skill Authoring** | Manual markdown/YAML editing | **Conversational Prompt Authoring & Pattern Extraction** directly from code |
| **Execution Architecture** | Single-threaded sequential agent | **Parallel Multi-Subagents** with isolated git worktrees |
| **Coding Benchmark** | 54.0% (Sonnet) / 69.6% (Opus) | **63.7% DeepSWE first-pass accuracy** on Gemini 3.7 Flash |
| **Verification & Testing** | Manual terminal loops | **Automated Sandbox Execution & Inspectable Artifacts** (Plans, Diffs, Walkthroughs) |
| **Team Synchronization** | Individual local configurations | **Git-Native (`.agents/skills/`)** — clone once, entire team inherits all engineering skills |
| **Enterprise Quota** | Per-seat individual credit card billing | **Pooled Project Quota (\$10/\$15 per seat)** in Gemini Enterprise with spend caps |
