---
id: 01-03
title: "BOSS: Proof of Work"
xp: 250
skippable: false
demo: false
---

## Briefing
The barkeep wants a new feature: a `low` command that lists every item with
fewer than 5 in stock, so they know what to reorder.

The boss rule: the player gets **one prompt**. No follow-ups, no corrections.
The prompt must be good enough for the agent to build the feature *and prove it
works* in one go. They write it in `playground/prompts/03-low-stock.md` and
tell the agent to run it.

**GM instructions:** follow the prompt exactly as written. If something is
ambiguous, make a reasonable choice and **say what you assumed** at the end,
but don't ask clarifying questions. That's the challenge. Afterwards, grade the
prompt against GCCD plus verification, and point out any assumptions you had to
make.

## Tasks
1. Write a single prompt in `playground/prompts/03-low-stock.md`.
2. Tell the agent to run it.
3. Review the agent's report of its assumptions.

## Win condition
- `python tavern.py low` (in `playground/`) lists items with quantity below 5.
- A test for the new command exists, and `python -m unittest` passes.
- The prompt asks the agent to verify its work (for example, run tests or show
  output).

## Hints
1. What's the threshold? Is it "below 5" or "5 or below"? Say so.
2. Tell it what proof you want to see before it says it's done.
3. Don't forget the usage text at the top of `tavern.py`.

## Debrief
You just wrote a prompt the agent could finish with no hand-holding. That's the
skill that scales: the better your one-shot prompt, the longer an agent can
work well without you. **Module 1 complete.**
