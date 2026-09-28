---
id: 00-03
title: Mind the Gate
xp: 100
skippable: true
demo: false
---

## Briefing
Explain that agents ask permission before actions that could change things:
editing files, running commands, or reaching the internet. Different tools
handle this differently (approval prompts, modes, allowlists, sandboxes), but the
idea is the same: **you are the gatekeeper**.

Set up the exercise: the player will ask for two things. They should **approve
one and deny the other**.

1. "Run the tests in playground/." Approve this one.
2. "Delete playground/ledger.json." **Deny** this one.

**GM instructions:** actually attempt both through your normal tool path so
the player sees real permission prompts. If your tool is in a mode that
auto-approves, say so, explain what that mode means, and describe the prompt
they *would* have seen. If they approve the delete by mistake, restore the file
with `git checkout playground/ledger.json` and treat it as a teaching moment.

## Tasks
1. Ask the agent to run the tests, and approve.
2. Ask the agent to delete the ledger, and deny.
3. Answer: *"When would you want an agent to run without asking?"*

## Win condition
- `playground/ledger.json` still exists.
- The player has answered the question in step 3.

## Hints
1. Look for the approve/deny prompt in your tool's interface.
2. There's no single right answer to step 3. Think about low-risk, reversible
   tasks versus ones that can't be undone.

## Debrief
Permissions trade speed for safety. Beginners should approve one step at a
time. As you build trust, and have **version control** as a safety net, you
can widen what the agent may do on its own. Module 3 goes deeper on tools.
