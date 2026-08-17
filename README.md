# 🚀 Google Antigravity & Gemini Skills Workshop: Unicomer Deep Dive

**Customer:** Grupo Unicomer (El Salvador / LATAM)  
**Lead Architect & Presenter:** Israel Castillo  
**Reviewers:** Alejandro & Mauricio  
**Target Audience:** Software Engineers, Tech Leads, Solutions Architects & DevOps Engineers at Unicomer  

---

## 📋 Executive Overview

This repository contains the complete technical enablement kit, slide content, hands-on lab modules, starter codebase, custom enterprise skills, and executive review package for the **Google Antigravity & Gemini Skills Deep Dive** for Unicomer.

The goal of this initiative is to demonstrate the paradigm shift from traditional AI code completion (Copilots) to **Autonomous Agentic Software Engineering (Antigravity & Gemini 3.7 Flash)**, equipping Unicomer developers to build, refactor, test, and govern enterprise applications with zero friction and measurable acceleration.

---

## 📂 Project Structure

```tree
unicomer-antigravity-workshop/
├── README.md                                    # This master index & overview
├── 01_REVIEW_PACKAGE_ALEJANDRO_MAURICIO.md      # Review package & executive briefing for Friday sync
├── 02_WORKSHOP_SLIDE_DECK_CONTENT.md           # Slide-by-slide technical deck content & speaker notes
├── 03_VSCODE_AND_TOOLING_ROADMAP_RESEARCH.md   # VS Code extension research, roadmap & enterprise config
├── custom-skills/                               # Reusable Gemini/Antigravity Enterprise Skills
│   ├── unicomer-credit-policy/
│   │   └── SKILL.md                            # Unicomer retail credit validation skill
│   └── unicomer-api-standards/
│       └── SKILL.md                            # Enterprise REST/API contract enforcement skill
├── labs/                                        # Step-by-step hands-on developer labs
│   ├── LAB_01_ANTIGRAVITY_ESSENTIALS.md        # Lab 1: Setup, Navigation & Plan-Act-Verify Loop
│   ├── LAB_02_CUSTOM_SKILLS_AND_RULES.md       # Lab 2: Building & Triggering Custom Skills
│   ├── LAB_03_AUTONOMOUS_SUBAGENTS.md          # Lab 3: Multi-Agent Parallel Refactoring & Testing
│   └── unicomer-sample-app/                    # Practical codebase for hands-on exercises
│       ├── main.py                             # FastAPI Retail Credit & Loyalty Service
│       ├── requirements.txt                    # App dependencies
│       ├── test_main.py                        # Automated test suite
│       └── README.md                           # Developer instructions for the lab app
```

---

## 🎯 Key Workshop Objectives

1. **Demystify Autonomous Agentic Engineering**: Contrast 1st gen AI copilots (line autocomplete) with Antigravity’s 3rd gen agentic platform (Plan → Act → Verify loop with subagents and sandboxed execution).
2. **Hands-On Frictionless Workflow**: Experience Antigravity across surfaces: **Antigravity 2.0 (GUI)**, **Antigravity CLI (Terminal)**, and **VS Code IDE Integration**.
3. **Enterprise Gemini Skills & Rules**: Teach Unicomer teams how to codify their architectural guidelines, security policies, and retail business rules into reusable `SKILL.md` and `AGENTS.md` assets.
4. **Enterprise Governance & Quotas**: Explain Gemini Enterprise pooled quotas ($10/$15 tier pooling per project), spend caps, strict sandboxing, MCP server whitelisting, and telemetry.
5. **Pilot Adoption Validation**: Run the hands-on lab with a pilot developer group to gather velocity metrics and feedback.

---

## ⏱️ Proposed Workshop Agenda (2.5 - 3 Hours)

| Time | Module | Format | Key Topics |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:30** | **Part 1: The Agentic Revolution & Architecture** | Presentation | • Evolution: Copilot vs Interactive vs Full Agentic<br>• Gemini Enterprise & Antigravity Suite<br>• Gemini 3.7 Flash Benchmarks & Cost/Task |
| **00:30 - 00:50** | **Part 2: Antigravity Surfaces & Tooling** | Demo & Tech Deep Dive | • Antigravity 2.0 GUI (Artifacts, Voice, Task boards)<br>• Antigravity CLI & Custom Slash Commands<br>• VS Code Plugin GA Roadmap & ADC Integration |
| **00:50 - 01:30** | **Part 3: Hands-On Lab 1 & 2** | Interactive Lab | • **Lab 1**: Plan-Act-Verify with `unicomer-sample-app`<br>• **Lab 2**: Authoring Custom Gemini Skills & AGENTS.md rules |
| **01:30 - 02:10** | **Part 4: Hands-On Lab 3 (Advanced Multi-Agent)** | Interactive Lab | • Spawning parallel subagents (Refactorer, Tester, Reviewer)<br>• Sandboxed execution & automated browser/API verification |
| **02:10 - 02:30** | **Part 5: Governance, Quotas & Next Steps** | Discussion & Q&A | • Pooled Quotas ($10/$15), Spend Caps & Audit Telemetry<br>• Next steps for pilot onboarding and VS Code rollout |

---

## 🚀 Quick Start for Facilitators

1. **Pre-requisites Check**:
   - Verify attendees have Google Cloud credentials / Gemini Enterprise access.
   - Ensure local dev environments have Python 3.10+, Docker (or local venv), and VS Code / Antigravity CLI.
2. **Review Deliverables**:
   - Read [`01_REVIEW_PACKAGE_ALEJANDRO_MAURICIO.md`](file:///usr/local/google/home/israelcastillo/gcp-projects/unicomer-antigravity-workshop/01_REVIEW_PACKAGE_ALEJANDRO_MAURICIO.md) prior to Friday alignment.
   - Review presentation slides in [`02_WORKSHOP_SLIDE_DECK_CONTENT.md`](file:///usr/local/google/home/israelcastillo/gcp-projects/unicomer-antigravity-workshop/02_WORKSHOP_SLIDE_DECK_CONTENT.md).
   - Review tooling & plugin details in [`03_VSCODE_AND_TOOLING_ROADMAP_RESEARCH.md`](file:///usr/local/google/home/israelcastillo/gcp-projects/unicomer-antigravity-workshop/03_VSCODE_AND_TOOLING_ROADMAP_RESEARCH.md).
