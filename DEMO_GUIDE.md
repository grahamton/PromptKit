# PromptKit Demo Guide

Use this flow to walk someone through PromptKit in 5-7 minutes.

## 1. Frame the Problem (1 min)
- Say: "PromptKit turns vague prompt issues into diagnosed, standardized fixes. We start with two sentences."
- Show the Seed and Friction for the scenario (e.g., TravelMate, SnackSmith).

## 2. Run the Iterate Card (2 min)
- In terminal (auto-select):
  `promptkit iterate --seed "..." --friction "..." --pattern auto --ascii`
- Narrate what the output gives:
  - Diagnosis - what's actually going wrong.
  - Fix - rules to insert; Prompt patch lines go straight into the prompt.
  - Validation - how to test it right away.
- Point out this works even without seeing the original prompt.

- Optional: Forced Diversification example (bias/coverage flows):
  `promptkit iterate --seed "Recommender helps pick keycap sets" --friction "Over-index on keyboards; needs diverse coverage beyond feed bias" --pattern forced-diversification --ascii`

## 3. Show the Plan (1-2 min)
- Run:
  `promptkit plan --seed "..." --friction "..." --pattern constraint-ledger --ascii`
- Highlight the headings (Context, Objective, Flow, Reasoning Path, Output).
- Emphasize "Reasoning Path" - six causal steps that explain why the change matters.

## 4. Print a Ticket (1 min)
- Run:
  `promptkit ticket --seed "..." --friction "..." --client "ClientName" --ascii`
- Say: "This is the shareable brief for teammates - problem, fix, success checks."

## 5. Web UI (optional, 1 min)
- Run locally: `uvicorn webapp.main:app --reload --port 8000` then open `http://localhost:8000`
- Use a preset (SnackSmith, Bard, etc.), click Run
- Show: Markdown-rendered output, copy/download, Human summary, Where to place sections, Compare (enable with `?flags=compare`)
- Pattern field: leave blank for auto, or try `forced-diversification`

## 6. Show the Business Runner (optional, 1 min)
- In PowerShell: `./promptkit-run.ps1`
- Enter the same Seed/Friction live to show the low-friction path for non-technical users.

## 6b. Dev Test Runner (optional, 30 sec)
- On Windows: `./dev-test.ps1` (creates venv, installs deps, runs tests)

## 7. Close with Outcomes
- PromptKit delivers: a fix, the why, and a handoff brief from two sentences.
- Works across prompts/models, because it focuses on reasoning patterns, not raw prompt text.
- Stop guessing; start diagnosing.
