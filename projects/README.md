# Project Builder

Each learner's practice project is **generated in Module 0** from a short
interview about work they actually did in the last two weeks. This file is the
guide's specification for that interview and for the project it builds.
Exercises refer to the project through **task slots** (`P0.1` … `P6.1`).

If the learner can't think of anything, or wants to move faster, use a
scenario from [examples.md](examples.md) instead.

## 1. Confidentiality (always applies)
- Before the interview, tell the learner: *"Describe the **kind** of work, not
  the specifics. Don't share client names, real figures, or confidential
  documents."*
- If they share something sensitive anyway, don't write it into any file.
  Replace it with a realistic stand-in (for example, "Client A", a made-up
  industry, invented figures).
- All data in the project is **synthetic**.

## 2. The interview (about 2 minutes, one question at a time)
1. **What did you work on in the last two weeks?** Pick one piece of work: a
   deliverable, analysis, feature, fix, or report.
2. **What went in and what came out?** Inputs (data, documents, systems, code)
   and the output (report, deck, model, feature).
3. **What was slow, tedious, or error-prone?** What did you have to wait on
   someone else for?
4. *Engineers only:* **Which language or stack?** Check that it's installed
   (for example `python --version`). If it isn't, or you're unsure, default to
   Python.

Then propose the scenario in **three lines** (what the project is, what's in
it, and what they'll do with it) and wait for the learner to confirm or adjust
it.

## 3. What to build
Keep it small: a person should be able to understand it in 2 minutes. Around
3–8 files.

**Everyone**
- `workspace/PROJECT.md`, visible to the learner: the scenario in plain
  language, a list of files, and **how to verify work** in this project.
- `save/project-key.md`, for the guide only: the concrete task for every slot
  below, including where each planted issue is. Tell the learner that this file
  is the answer key and suggest they don't open it.

**Engineer persona**
- A small codebase in their language, modelled on the work they described.
- A test suite that runs with tools already installed. Run it once to confirm
  it works. Tests must pass at the start; planted bugs are in areas the tests
  don't yet cover.
- Verification = run the tests.

**Business persona**
- Source data (CSV or Markdown tables) plus supporting documents (notes,
  briefs, a template), modelled on the work they described.
- An existing output (a report or summary) that contains planted errors.
- `workspace/CHECKS.md`: a list of checks, each tying an output figure or claim
  to its source (for example, "Total revenue in report = sum of `revenue` in
  `data/sales.csv`").
- Verification = the agent runs through `CHECKS.md` and shows its working.

## 4. Task slots
Plant something for each slot and describe it in `save/project-key.md`.

| Slot | Module | What the project must provide |
|------|--------|-------------------------------|
| `P0.1` | 0 | One safe action (run the checks) and one destructive action to refuse (delete a key input file) |
| `P1.1` | 1 | A defect with a symptom that's easy to see (a crash, or a wrong total) |
| `P1.2` | 1 | A change involving at least one real design choice. Name the choice in the key. |
| `P1.3` | 1 | A small new feature or deliverable that can be verified |
| `P2.1` | 2 | Facts that belong in a memory file: how to run and check the project, conventions, definitions, known issues |
| `P2.2` | 2 | A task large enough to hand off halfway |
| `P3.1` | 3 | A repeated workflow that should become a skill (a release checklist, a monthly report) |
| `P4.1` | 4 | An external system an MCP server could connect this work to (a note of what fits; nothing to build) |
| `P6.1` | 6 | A capstone task that uses every module |

Where possible, tie the planted issues to the **slow or error-prone** parts the
learner described in question 3. That's where the course will feel most useful
to them.
