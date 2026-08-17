# 🎙️ Live Demo Cheat Sheet: Antigravity 2.0 & Subagents (Unicomer)

**Target Audience:** Alejandro, Mauricio & Unicomer Engineering Leads  
**Presenter:** Israel Castillo  
**Core Storyline:** Demonstrating the leap from simple copilots to **Autonomous Multi-Agent Engineering** using Antigravity 2.0 and **Gemini 3.7 Flash** on a realistic Unicomer Retail Microservice (`La Curacao`, `Gollo`, `Emma`).

---

## ⏱️ Live Demo Timeline (12 - 15 Minutes Total)

```
[00:00 - 02:00] Act 1: Set the Stage & Generate Implementation Plan
[02:00 - 06:00] Act 2: Launch Parallel Subagents (Logic, Security, QA)
[06:00 - 08:00] Act 3: Sandbox Verification & Walkthrough Artifact
[08:00 - 11:00] Act 4: Prompt-Driven Custom Skill Creation Live
[11:00 - 13:00] Act 5: The Claude vs Gemini 3.7 Flash Angle
[13:00 - 15:00] Q&A & Transition to Developer Hands-on Lab
```

---

## 🎬 Act 1: Set the Stage & Implementation Plan (Plan)

### 🗣️ Speaker Intro:
> *"Instead of writing code line-by-line with autocomplete, watch what happens when we give Antigravity a high-level engineering requirement for our retail credit service."*

### 📋 Prompt 1:
```text
Analyze this repository. We need to upgrade our credit evaluation engine in main.py:
1. Replace the linear installment estimate with the formal French amortization formula: Cuota = P * [ r(1+r)^n ] / [ (1+r)^n - 1 ].
2. Enforce the 2026 Unicomer retail policy: Max automated financing is $3,500 for LA_CURACAO, $2,500 for GOLLO, $1,500 for EMMA, and $1,000 for RADIOSHACK.
3. Fix the critical PII logging issue where DUI/NIT and phone numbers are currently exposed in plaintext.

Please generate an Implementation Plan detailing the affected functions, testing strategy, and risk assessment. Do not modify code yet.
```

### 👁️ What They See:
- Antigravity scans the entire repo and generates a live `implementation_plan.md` artifact.
- Show them the interactive plan and click **"Proceed"** (or type *"Plan approved, proceed with parallel subagents"*).

---

## 🤖 Act 2: Spawning Parallel Subagents (Act)

### 🗣️ Speaker Talking Point:
> *"Here is where Antigravity 2.0 leaves single-threaded copilots behind. We delegate the work to three specialized subagents running concurrently."*

### 📋 Prompt 2:
```text
Execute this implementation plan using 3 specialized subagents in parallel:
- Subagent 1 (Role: 'Financial Logic Engineer'): Refactor main.py to implement the French amortization formula and brand financing caps.
- Subagent 2 (Role: 'Security & Compliance Auditor'): Audit main.py to mask all customer PII (DUI/NIT and phone) in application logs.
- Subagent 3 (Role: 'QA Test Automation Engineer'): Expand test_main.py to add unit test coverage for brand caps, boundary conditions, and VIP tiers.

Coordinate and report back when all subagents complete their work.
```

### 👁️ What They See:
- Three subagents spawn simultaneously in the Antigravity 2.0 task tray.
- Live progress updates showing each subagent working in parallel worktrees without blocking the UI.

---

## 🛡️ Act 3: Sandbox Verification & Change Walkthrough (Verify)

### 🗣️ Speaker Talking Point:
> *"Antigravity doesn't just write code and hope it works. It enters the Verify phase in an isolated sandbox."*

### 📋 Prompt 3:
```text
Execute pytest on the test suite in the sandbox to verify that 100% of tests pass. Then generate a comprehensive walkthrough.md artifact summarizing all changes made.
```

### 👁️ What They See:
- Terminal command executed safely in the sandbox.
- Tests passing 100%.
- A polished `walkthrough.md` artifact with code diffs, security fixes, and architectural notes.

---

## ⚡ Act 4: Creating a Custom Gemini Skill Live via Prompt

### 🗣️ Speaker Talking Point:
> *"How do you ensure every developer in Unicomer follows these standards automatically? We create an enterprise Gemini Skill with one prompt."*

### 📋 Prompt 4:
```text
Create a new custom skill in .agents/skills/unicomer-loyalty-rules/SKILL.md that codifies Unicomer's loyalty reward multipliers: 1x for Standard, 1.5x for Silver, 2x for Gold, and 3x for Platinum. Include rules requiring that points calculations are always logged with masked customer IDs.
```

### 👁️ What They See:
- Antigravity authors the `SKILL.md` with YAML frontmatter.
- The new skill immediately registers as a project-level capability and custom slash command!

---

## 🥊 Act 5: The Claude vs. Gemini 3.7 Flash Talking Points

### When Unicomer asks about Claude models:

| Dimension | Claude (Sonnet / Opus) | Gemini 3.7 Flash in Antigravity |
| :--- | :--- | :--- |
| **Model Ecosystem Support** | Supported via Gemini Enterprise Agent Platform | Native frontier engine co-optimized for Antigravity harness |
| **DeepSWE Benchmark (Coding Accuracy)** | 54.0% (Sonnet) / 69.6% (Opus) | **63.7% first-pass accuracy** at Flash-tier economics |
| **FrontierCode 1.1 (Production Quality)** | 42.7% (Sonnet) | **43.6%** (Gemini 3.7 Flash) |
| **Inference Latency** | Higher latency on multi-tool chains | **Ultra-low latency** optimized on Google AI Hypercomputer (TPU v5) |
| **Cost / Task for Long Horizons** | \$10 - \$15 per heavy multi-file refactor | **Fraction of the cost** — fits comfortably within the \$10/\$15 monthly pooled quota |
