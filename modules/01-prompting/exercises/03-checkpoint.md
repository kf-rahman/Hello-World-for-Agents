---
id: 1.3
title: "Checkpoint: One Prompt, Verified Result"
minutes: 8
skippable: false
demo: false
project_slot: P1.3
---

## Purpose
Write one prompt good enough for the agent to finish a task and prove it works,
with no follow-up messages.

## Guide instructions
Describe the `P1.3` task. The rule: the learner gets **one prompt**, written in
`workspace/prompts/1.3.md`.

Carry out the prompt exactly as written. Don't ask clarifying questions. Where
something is unclear, make a reasonable choice and **list your assumptions** at
the end. Then review the prompt against Goal, Context, Constraints, Done when,
and verification, and point out each place where you had to assume something.

## Learner steps
1. Write one prompt in `workspace/prompts/1.3.md`.
2. Tell the agent to run it.
3. Read the list of assumptions.

## Completion check
- The `P1.3` task is complete and the project's verification passes.
- The prompt asks the agent to verify its work, for example by running tests
  or checking figures against the source.

## Hints
1. Name the limits and edge cases explicitly.
2. Say what proof you want to see before the agent reports that it's done.

## Takeaway
The better your first prompt, the longer an agent can work well without you.
That skill matters more as tasks get bigger.
