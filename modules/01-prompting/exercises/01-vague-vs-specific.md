---
id: 1.1
title: Vague vs Specific
minutes: 10
skippable: false
demo: false
project_slot: P1.1
---

## Purpose
Show what an agent does with a vague prompt, then fix the prompt using Goal,
Context, Constraints, Done when.

## Guide instructions
**Round 1.** Don't reveal the `P1.1` defect yet. Ask the learner to send exactly:
`fix the problem in workspace`.

Respond as an agent would to a vague request: pick the issue that seems most
likely, say what you assumed, and **propose** a change without making it. Then
ask: *"Is that the problem you meant? What did I have to guess?"*

**Round 2.** Describe the `P1.1` symptom (what happens, and what should happen
instead). Ask the learner to write a prompt in `workspace/prompts/1.1.md` using
Goal, Context, Constraints, Done when, and then tell you to run it.

## Learner steps
1. Send the vague prompt and look at what the agent assumed.
2. Write a structured prompt in `workspace/prompts/1.1.md`.
3. Ask the agent to run it.

## Completion check
- `workspace/prompts/1.1.md` has a clear goal, points to the relevant file or
  data, gives at least one constraint, and says how to confirm it's done.
  Judge the content, not the headings.
- The `P1.1` defect is fixed and the project's verification passes.

## Hints
1. Start with the symptom: what you did, what happened, and what should have happened.
2. Point the agent at the specific file or data involved.
3. Give a checkable "done when", for example: "a test covers it and all tests
   pass" or "the corrected total matches the source file."

## Takeaway
The vague prompt made the agent guess. The specific prompt gave it a checklist.
Adjust how much detail you give to the size of the task.
