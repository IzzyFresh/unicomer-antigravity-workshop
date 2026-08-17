# 🛠️ Google Antigravity 2.0: Developer Hands-On Labs (Unicomer)

**Target Audience:** Software Engineers, Backend Developers, Tech Leads & DevOps at Grupo Unicomer  
**Core Tooling:** **Google Antigravity 2.0 (GUI)** + **Visual Studio Code Extension**  
**Underlying Engine:** **Gemini 3.7 Flash** (Frontier Agentic Reasoning, 63.7% DeepSWE)

---

## 🎯 Hands-On Workshop Mission

This repository is a **100% code-first, interactive laboratory** designed to teach Unicomer engineers how to leverage **Google Antigravity 2.0** for autonomous software development. 

Instead of traditional copilots that only autocomplete single lines of code, you will experience **autonomous agentic workflows**: planning multi-file refactors, authoring reusable software engineering skills via natural language prompts, orchestrating parallel subagents across isolated Git worktrees, and validating code inside secure sandboxes.

---

## 📂 Repository Structure

```tree
unicomer-antigravity-workshop/
├── DEMO_PROMPT_CHEATSHEET.md                    # Copy-paste prompts & talk track for facilitators
├── 01_REVIEW_PACKAGE_ALEJANDRO_MAURICIO.md      # Hands-on enablement brief for engineering leadership
├── 03_VSCODE_AND_TOOLING_ROADMAP_RESEARCH.md   # VS Code extension architecture & ADC configuration
├── custom-skills/                               # Enterprise Engineering Skills (Drop-in ready)
│   ├── fastapi-clean-architecture/
│   │   └── SKILL.md                            # Clean Architecture scaffolding & layer separation
│   ├── pytest-mock-generator/
│   │   └── SKILL.md                            # Automated Pytest fixtures, mocks & boundary testing
│   ├── unicomer-credit-policy/
│   │   └── SKILL.md                            # Retail credit policy & brand caps
│   └── unicomer-api-standards/
│       └── SKILL.md                            # REST API contract & OpenAPI standards
└── labs/                                        # Step-by-step interactive developer labs
    ├── LAB_01_ANTIGRAVITY_ESSENTIALS.md        # Lab 1: Antigravity 2.0 GUI, VS Code & Plan-Act-Verify
    ├── LAB_02_CUSTOM_SKILLS_AND_RULES.md       # Lab 2: Prompt-Driven Engineering Skills Authoring
    ├── LAB_03_AUTONOMOUS_SUBAGENTS.md          # Lab 3: Local Agents, Parallel Subagents & Sidecars
    └── unicomer-sample-app/                    # Practical FastAPI Retail Credit Microservice
        ├── main.py
        ├── test_main.py
        ├── requirements.txt
        └── README.md
```

---

## 🚀 The 3 Hands-On Labs

| Lab | Developer Focus | Key Takeaways & Deliverables |
| :--- | :--- | :--- |
| **[Lab 1: The Plan-Act-Verify Loop](labs/LAB_01_ANTIGRAVITY_ESSENTIALS.md)** | *Interface & Autonomous Workflow* | Connect Antigravity 2.0 with VS Code, generate interactive `implementation_plan.md` artifacts, review atomic code diffs, and verify fixes in the sandbox. |
| **[Lab 2: Prompt-Driven Engineering Skills](labs/LAB_02_CUSTOM_SKILLS_AND_RULES.md)** | *Architecture & Quality Automation* | Use natural language prompts to create reusable coding skills (`fastapi-clean-architecture`, `pytest-mock-generator`), refactor monolithic code, and sync skills across the team via Git (`.agents/skills/`). |
| **[Lab 3: Local Agents, Subagents & Sidecars](labs/LAB_03_AUTONOMOUS_SUBAGENTS.md)** | *Parallel Multi-Agent Scale* | Define local agents, spawn 3 parallel subagents (Architect, Security Auditor, QA) working in isolated Git worktrees, configure background quality sidecars, and generate a final `walkthrough.md` artifact. |

---

## ⚡ Quick Start for Developers

* **Visual Studio Code Extension:**
  * 📦 **VS Code Marketplace:** [https://marketplace.visualstudio.com/items?itemName=Google.antigravity](https://marketplace.visualstudio.com/items?itemName=Google.antigravity)
  * ⚡ **One-Click Install in VS Code:** [`vscode:extension/Google.antigravity`](vscode:extension/Google.antigravity)
  * 🌐 **Official Portal:** [https://antigravity.google](https://antigravity.google)

1. **Clone this repository into your workspace:**
   ```bash
   git clone https://github.com/IzzyFresh/unicomer-antigravity-workshop.git
   cd unicomer-antigravity-workshop/labs/unicomer-sample-app
   ```
2. **Open the project in Visual Studio Code:**
   ```bash
   code .
   ```
3. **Open Antigravity 2.0 (GUI):**
   * Select the `unicomer-sample-app` workspace.
   * Open **[Lab 1 Guide](labs/LAB_01_ANTIGRAVITY_ESSENTIALS.md)** and start interacting with your Lead Agent!
