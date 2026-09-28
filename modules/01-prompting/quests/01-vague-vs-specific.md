---
id: 01-01
title: Vague vs Specific
xp: 100
skippable: false
demo: false
---

## Briefing
Tell the player there's a bug in the Tavern Ledger: selling an item that isn't
in stock (`python tavern.py sell wine 1`) crashes with a `KeyError`.
**Don't tell them this yet.** First, run the experiment below.

**Round 1:** ask the player to send exactly: `fix the bug in playground`

**GM instructions:** for Round 1 only, act the way an under-specified agent
really would. Pick whichever issue looks most likely to you, say what you
assumed, and **propose** a change without applying it. Then ask: *"Was that the
bug you meant? What did I have to guess?"*

**Round 2:** reveal the real bug. Ask the player to write a better prompt in
`playground/prompts/01-fix-sell.md` using the GCCD pattern (Goal, Context,
Constraints, Done-when), then send it to you by saying "run the prompt in
playground/prompts/01-fix-sell.md".

## Tasks
1. Send the vague prompt and see what the GM guesses.
2. Write a GCCD prompt in `playground/prompts/01-fix-sell.md`.
3. Have the agent run it.

## Win condition
- `playground/prompts/01-fix-sell.md` exists and has a clear goal, names the
  file or function, gives at least one constraint, and says how to tell it's
  done. (Judge the content, not the headings.)
- `python tavern.py sell wine 1` (run in `playground/`) prints a friendly error
  instead of a traceback.
- `python -m unittest` passes in `playground/`.

## Hints
1. Start with the *symptom*: what command, what happened, what should happen.
2. Point at the code: `playground/tavern.py`, the `sell()` function.
3. A good "done when": "there's a test for selling an unknown item, and all
   tests pass."

## Debrief
The vague prompt made the agent **guess**, and guesses compound over many
steps. The specific prompt turned a guess into a checklist. Keep GCCD in your
back pocket, but don't treat it as a ritual. Small tasks need less, big ones
need more.
