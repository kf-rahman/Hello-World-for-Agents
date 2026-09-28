---
id: 01-02
title: Plan Before You Build
xp: 100
skippable: true
demo: false
---

## Briefing
New bug report from the barkeep: *"We sold 50 ales when we only had 40. Now the
ledger says we have -10 ale!"*

This time the player shouldn't let the agent start coding right away. They'll ask
for a **plan first**, review it, push back on at least one point, and only then
approve.

Mention that some tools have a built-in plan mode (for example, Claude Code's
plan mode). In any tool, you can simply say "don't change anything yet, just
give me a plan."

**GM instructions:** when asked for a plan, give a short numbered plan and
include one reasonable but debatable choice (for example, whether overselling
should raise an error or sell what's left). Don't write code until the player
approves.

## Tasks
1. Ask the agent for a plan to prevent overselling, with no code yet.
2. Push back on or change at least one step of the plan.
3. Approve, and let the agent carry it out.

## Win condition
- Selling more than the stock no longer makes the quantity negative.
- There's a test covering overselling, and `python -m unittest` passes in `playground/`.
- The player changed or questioned at least one step of the plan (check the
  conversation).

## Hints
1. Try: "Don't write code yet. Give me a plan to stop overselling in playground/tavern.py."
2. Look for choices the plan makes *for* you. Is that what the barkeep would want?

## Debrief
A plan is a cheap draft. Five seconds of reviewing it can save five minutes
of undoing changes. For anything that touches more than one file, plan first.
