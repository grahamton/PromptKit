# PromptKit: The Prompt System Diagnostics Framework

Stop guessing and start fixing by diagnosing root causes and standardizing validated fixes.

Prompt engineers, product managers, and ops teams waste time on trial-and-error prompt tuning and can’t explain why a change worked. **PromptKit** solves this by explaining *why* each prompt change is made, providing clear, testable, and reusable artifacts.

## Key Benefits

* **Root-Cause Clarity:** See the exact mismatch between your prompt's goal and the model's actual behavior to surface breakdowns in reasoning, tone, grounding, pacing, and success checks.
* **Actionable, Standardized Fixes:** Every fix is a reusable, testable artifact (**Iterate Card**) with a clear diagnosis, rules to drop into your prompt, and validation scenarios.
* **Story-Ready Plans:** Generate one-page summaries (**Plan**) that explain the causal reasoning chain behind a change for stakeholders.
* **Seamless Team Handoffs:** Use filled **Tickets** and the PowerShell runner to empower PMs, ops, or subject-matter experts to self-serve prompt improvements.

## Overview
PromptKit helps you improve prompts by explaining why each change is made. For prompt engineers, product managers, and ops teams who waste time on trial-and-error prompt tuning and can’t explain why a change worked. It outputs small, deterministic artifacts:
- Iterate Card: Diagnosis -> Fix -> Validation
- Plan: Context, Objective, Flow, Reasoning Path, Output
- Ticket: A brief template tying a real problem to a testable PromptKit fix

> Note: This is an exploratory test product I'm using to learn and experiment with tooling.

## How It Works
- PromptKit is a prompt system diagnostics framework, not a syntax fixer. Stop guessing; start diagnosing.
- It compares intended behavior against real output to surface breakdowns in reasoning, tone, grounding, pacing, and success checks.
- Two operating lenses:
  - **Prompt Repair Layer** - diagnose and tighten a single prompt or template.
  - **System Diagnostic Layer** - trace control gaps across agents, retrieval, and orchestration flow.
- Guiding principle: *prompts are systems, not sentences*.

## What You Get
- **Root-cause clarity** – see the exact mismatch between goal and behavior.
- **Actionable fixes** - each Iterate Card standardizes a single change into a reusable, testable artifact: diagnosis, rules to drop into your prompt, and validation scenarios.
- **Story-ready plans** – one-page summaries explain the reasoning chain for stakeholders.
- **Team handoffs** – Tickets and the PowerShell runner let PMs, ops, or subject-matter experts self-serve improvements.

## Where It’s Already Helping
- **SnackSmith kiosk** – mapped “sweet but airy” to concrete flavor controls and tests.
- **TravelMate trip planner** – translated emotional language (“quiet, inspiring”) into budget and timeline constraints.
- **BrewBuddy barista** – kept allergy and taste preferences in a live ledger to prevent remakes.
- **Myco grower assistant** – clarified “fuzzy but fine” jars into safe vs. contaminated actions.

## Install
- Editable install (recommended):
  - `python -m pip install -e .`

## Developer Quickstart
- Install dev tools: `python -m pip install -e .[dev]`
- Lint: `ruff check .`
- Format check: `black --check .` (format with `black .`)
- Tests: `pytest -q` or `./dev-test.ps1` on Windows (creates venv, installs deps, runs tests)
- Run CLI locally:
  - `promptkit plan --seed "demo" --friction "demo" --ascii`
  - `promptkit ticket --seed "demo" --friction "demo" --ascii`
  - `promptkit iterate --seed "demo" --friction "demo" --ascii`

## CI
- GitHub Actions runs on push and PR: ruff, black --check, pytest.
- Protect `main` by requiring the CI job to pass (Settings → Branches).

## Web App (Optional UI)
- Run locally:
  - `python -m pip install -r webapp/requirements.txt`
  - `uvicorn webapp.main:app --reload --port 8000`
  - Open `http://localhost:8000`
- Flags (optional):
  - Query: `?flags=compare,feedback`
  - Env: `PK_UI_COMPARE=1`, `PK_UI_FEEDBACK=1`
- Useful routes: `/modes`, `/research`, `/health`
- Presets: SnackSmith, Bard, Chef, Roomba, Weather, TravelMate
- Features: Markdown-rendered output, copy/download, Compare (flag), Download Session/Feedback (no telemetry)

## Commands
### iterate
Generate a single Iterate Card from a seed and a friction point.
- Usage:
  - `promptkit iterate --seed "..." --friction "..." [--pattern <name>[,<name>...]|auto] [--ascii] [--json]`
- Patterns (no scoring): `constraint-ledger`, `contrastive-clarify`, `exemplar-propose`, `override-hook`, `state-bag`, `slot-filling`, `forced-diversification`
- Combine patterns by comma to merge behaviors deterministically.
- Auto-select: pass `--pattern auto` (or leave Pattern blank in the UI) to choose one or two patterns from cues in your Friction text.
- Example (SnackSmith):
  - `promptkit iterate --seed "SnackSmith flavor assistant helps build custom snacks from natural-language taste descriptions." --friction "Misinterprets adjectives; mixes mismatched flavors; lacks constraints memory; no fast staff override." --pattern constraint-ledger --ascii`
 - Example (Combined):
   - `promptkit iterate --seed "..." --friction "..." --pattern "constraint-ledger,contrastive-clarify" --ascii`
 - Output includes a Human summary and "Where to place in your prompt" section to help you drop lines under Rules/Policy, State/Memory, Clarifiers, Overrides, Interaction/Output.

### plan
Produce a compact plan that shows causal reasoning behind the change.
- Usage:
  - `promptkit plan --seed "..." --friction "..." [--pattern <name>] [--ascii]`
- Example (SnackSmith):
  - `promptkit plan --seed "SnackSmith flavor assistant helps build custom snacks from natural-language taste descriptions." --friction "Misinterprets adjectives; mixes mismatched flavors; lacks constraints memory; no fast staff override." --pattern constraint-ledger --ascii`

### ticket
Print a filled PromptKit ticket to frame work quickly.
- Usage:
  - `promptkit ticket --seed "..." --friction "..." [--client "..."] [--prompt_brief "..."] [--real_problem "..."] [--test_problem "..."] [--goal "..."] [--success "..."]... [--ascii]`
- Example (SnackSmith minimal):
  - `promptkit ticket --seed "SnackSmith flavor assistant helps build custom snacks from natural-language taste descriptions." --friction "Misinterprets adjectives; mixes mismatched flavors; lacks constraints memory; no fast staff override." --client "SnackSmith" --ascii`

## Patterns (no scoring)
- constraint-ledger: Keep a running list of constraints (include/avoid/not-too/vibes); echo and confirm before action.
- contrastive-clarify: Ask one either/or to disambiguate a term; reflect choice; proceed.
- exemplar-propose: Offer two tiny, concrete options that fit constraints; let the user pick or tweak.
- override-hook: Simple staff commands (override/lock/reduce/reset); apply immediately and echo.
- state-bag: Keep explicit state (goal/include/avoid/not_too/memory/next_step/confirmed); echo updates; confirm before finalizing.
- slot-filling: Ask only for missing required fields; echo and confirm summary before actions.
- forced-diversification: Extract 3+ non-primary interests; output two labeled recs (Balanced, Novelty) to counter feed/echo bias.

Advisory: pattern outputs include a short "Model considerations" section (guidance only) to help keep rules atomic, echoed succinctly, and consistently placed.

See also: Why These Patterns? (run the UI at `http://localhost:8000` and open `/research`).

## Notes
- Use `--ascii` to avoid Unicode rendering issues in terminals.
- In PowerShell, prefer double quotes around arguments; escape embedded double quotes.

## Status
- iterate, plan, and ticket commands are implemented. More patterns and helpers can be added as needed.

Why Three Modes? (run the UI at `http://localhost:8000` and open `/modes`).

## Business Runner (PowerShell)
- From the repo root, run: `./promptkit-run.ps1`
- It will ask for:
  - Seed (one sentence)
  - Friction (one sentence)
  - Optional pattern (press Enter to auto)
- It prints an Iterate Card to your terminal (ASCII-safe). If the `promptkit` CLI is not installed, it runs from local source automatically.
- If you hit an execution policy warning, you can run once with: `powershell -ExecutionPolicy Bypass -File ./promptkit-run.ps1`

Troubleshooting
- "Python not found": install Python 3.9+ or install the CLI: `python -m pip install -e .`
- Missing dependency `typer`: `python -m pip install typer` (or install the CLI with `-e .`).
- Command not recognized `promptkit`: run the script again (it will use local source), or install the CLI: `python -m pip install -e .`

## Business Quick Start
- Provide two short lines (no tech needed):
  - Seed: what the assistant does and for whom (one sentence).
  - Friction: the biggest failure right now (one sentence).
- Pick the output you want:
  - Iterate Card: one targeted fix with how to validate it.
  - Plan: a clear, one‑page explanation of why the fix works.
  - Ticket: a brief to share with your team to kick off work.
- Ask a teammate to run the command examples above and send you the output, or copy/paste the output lines into your existing prompt.

See the step-by-step business guide: `GUIDE_BUSINESS.md`.

## Demo Playbook
- Want to show PromptKit live? Follow `DEMO_GUIDE.md` for a 5–7 minute walkthrough covering Iterate Card (including `auto` and `forced-diversification`), Plan, Ticket, the web UI (Markdown output), and the business/dev runners.

## Roadmap
- Future work (prompt ingestion, model considerations, validation tooling, team workflows) is tracked in `ROADMAP.md`.

## Changelog
- See `CHANGELOG.md` for unreleased changes and version history.
- Commit style: Conventional Commits (e.g., `feat:`, `fix:`, `docs:`) to make future release notes easier to generate.
