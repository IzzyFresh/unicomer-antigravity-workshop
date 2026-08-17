# 🎙️ Live Demo Cheat Sheet: Antigravity 2.0 & Skills (Unicomer)

**Target Audience:** Alejandro, Mauricio & Unicomer Engineering Leads (Users of Claude Code & modern IDEs)  
**Presenter:** Israel Castillo  
**Core Storyline:** Demonstrating the ease of **creating, extracting, and executing enterprise Skills in Antigravity 2.0 entirely through natural language prompts**, orchestrating parallel subagents, and comparing with Claude Code.

---

## ⏱️ Live Demo Timeline (12 - 15 Minutes Total)

```
[00:00 - 02:00] Act 1: Set the Stage & Implementation Plan in Antigravity 2.0
[02:00 - 05:00] Act 2: Prompt-Driven Skill Creation & Pattern Extraction Live
[05:00 - 09:00] Act 3: Launch Parallel Subagents (Logic, Security, QA)
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
Analyze this repository. We need to upgrade our credit evaluation engine in main.py:
1. Replace the linear installment estimate with the formal French amortization formula: Cuota = P * [ r(1+r)^n ] / [ (1+r)^n - 1 ].
2. Enforce the 2026 Unicomer retail policy: Max automated financing is $3,500 for LA_CURACAO, $2,500 for GOLLO, $1,500 for EMMA, and $1,000 for RADIOSHACK.
3. Fix the critical PII logging issue where DUI/NIT and phone numbers are currently exposed in plaintext.

Please generate an Implementation Plan detailing the affected functions, testing strategy, and risk assessment. Do not modify code yet.
```

---

## ⚡ Act 2: Creating Enterprise Skills Live via Prompts in Antigravity 2.0

### 🗣️ Speaker Talking Point:
> *"One of the main questions teams ask is: 'How easy is it to teach Antigravity our company standards compared to Claude Code?' In Antigravity 2.0, you create and extract skills with plain English or Spanish prompts. No manual YAML, no file boilerplates."*

### 📋 Prompt 2A (Create Skill from Scratch):
```text
Create a new custom skill in .agents/skills/unicomer-scoring-engine/SKILL.md that establishes Unicomer credit scoring rules:
- Credit scores range from 300 to 850.
- Scores >= 700 (Gold/Platinum) receive a 4% APR discount.
- Scores between 600 and 699 (Silver) receive a 2% APR discount.
- Scores < 600 require a co-signer or reject if DTI > 35%.
Format the skill with full YAML frontmatter, input/output schemas, and examples.
```

### 📋 Prompt 2B (Extract Skill from Active Code Pattern):
```text
Analyze how we mask customer DUI/NIT and phone numbers in main.py, and extract that into a reusable enterprise skill in .agents/skills/unicomer-pii-masking/SKILL.md so all Unicomer microservices follow the exact same security standard.
```

---

## 🤖 Act 3: Spawning Parallel Subagents in Antigravity 2.0

### 🗣️ Speaker Talking Point:
> *"Now we tell our Lead Agent to execute the work using parallel subagents. Each subagent gets its own focused role, prompt, and isolated git worktree."*

### 📋 Prompt 3:
```text
Execute our implementation plan and apply our new 'unicomer-scoring-engine' skill using 3 specialized subagents in parallel:
- Subagent 1 (Role: 'Financial Logic Engineer'): Refactor main.py to implement the French amortization formula, brand caps, and scoring engine.
- Subagent 2 (Role: 'Security & Compliance Auditor'): Apply the 'unicomer-pii-masking' skill across all logging points in main.py.
- Subagent 3 (Role: 'QA Test Automation Engineer'): Expand test_main.py with unit tests for brand caps, boundary conditions, and scoring tiers.

Coordinate and report back when all subagents complete their work.
```

---

## 🛡️ Act 4: Sandbox Verification & Walkthrough Artifact

### 🗣️ Speaker Talking Point:
> *"Antigravity verifies its own work inside a secure execution sandbox before handing it back to the developer."*

### 📋 Prompt 4:
```text
Execute pytest on the test suite in the sandbox to verify that 100% of tests pass. Then generate a comprehensive walkthrough.md artifact summarizing all changes, security fixes, and new skill definitions.
```

---

## 🥊 Act 5: Claude Code vs. Antigravity 2.0 Comparison for Developers

### Talking points for teams familiar with Claude Code:

| Capability | Claude Code | Google Antigravity 2.0 |
| :--- | :--- | :--- |
| **Skill Authoring** | Manual text file creation / prompt editing | **Conversational Prompt Creation & Pattern Extraction** from active code |
| **Execution Model** | Single-threaded sequential agent | **Parallel Multi-Subagents** with isolated worktrees |
| **Core SWE Benchmark** | 54.0% (Sonnet) / 69.6% (Opus) | **63.7% DeepSWE first-pass accuracy** on Gemini 3.7 Flash |
| **Verification & Testing** | Manual terminal loops | **Automated Sandbox Execution & Inspectable Artifacts** (Plans, Diffs, Walkthroughs) |
| **Team Synchronization** | Individual local configurations | **Git-Native (`.agents/skills/`)** — clone once, entire team inherits all skills |
| **Enterprise Quota** | Per-seat credit card billing | **Pooled Project Quota (\$10/\$15 per seat)** in Gemini Enterprise with spend caps |
