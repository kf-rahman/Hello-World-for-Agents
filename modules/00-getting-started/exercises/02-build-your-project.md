---
id: 0.2
title: Build Your Project
minutes: 5
skippable: false
demo: true
project_slot: all
---

## Purpose
Build the learner's practice project from their own recent work, and let them
watch the agent loop happen live while it's built.

## Guide instructions
Follow `projects/README.md` exactly.

1. **Confidentiality first.** Tell the learner to describe the *kind* of work,
   not specifics: no client names, real figures, or confidential documents.
2. **Interview.** Ask the questions from `projects/README.md` one at a time. If
   the learner can't think of anything or wants to move quickly, offer a
   scenario from `projects/examples.md`.
3. **Propose.** Summarize the scenario in three lines and wait for the learner to
   confirm it.
4. **Build (demo), and narrate the loop.** Before each action, say in one
   line what you're doing and why (for example, "Writing the source data
   first, so the report has something to be checked against"). Build the files,
   `workspace/PROJECT.md`, `workspace/CHECKS.md` (business) or the tests
   (engineer), and `save/project-key.md`. Run the verification once to show
   it works.
5. **Summarize.** Tell the learner how many actions you took, and point out:
   *"I read, wrote, ran something, looked at the result, and adjusted. That's
   the agent loop."* Tell them `save/project-key.md` is the answer key and
   suggest they don't open it.
6. Record the project in `save/save.md` (the scenario summary and verification
   method).

## Learner steps
1. Answer the interview questions, without confidential details.
2. Confirm or adjust the proposed scenario.
3. Watch the build and read `workspace/PROJECT.md`.

## Completion check
- `workspace/PROJECT.md` exists and describes the scenario, the files, and how
  to verify work.
- `save/project-key.md` has a task for every slot in `projects/README.md`.
- Verification runs successfully (the tests pass, or the checks in `CHECKS.md`
  can be run).
- None of the files contain anything the learner flagged as confidential.

## Hints
1. Think of anything you produced recently: a report, a model, a fix, an
   analysis. A rough description is enough.
2. Not sure? Ask for one of the example scenarios.

## Takeaway
You described your work in plain language, and the agent turned it into a
working project. That's the **agent loop**: read → decide → act → observe →
repeat.
