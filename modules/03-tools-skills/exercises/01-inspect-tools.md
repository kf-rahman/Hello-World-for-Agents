---
id: 3.1
title: Inspect the Tools
minutes: 5
skippable: true
demo: false
project_slot: none
---

## Purpose
Make tools concrete: see which ones the agent has and what one tool call
involves.

## Guide instructions
1. The learner asks you: "What tools do you have?" List them in plain language,
   grouped: read/search, edit, run commands, web, sub-agents, and anything
   connected through MCP.
2. The learner then asks you to do one small thing (for example, count the
   files in `workspace/`). Afterwards, break that single tool call down: which
   tool you chose, what input you passed, what came back, and how you used the
   result.
3. Show the learner where their tool keeps its permission settings, and help
   them allowlist one safe, frequently used action (such as the project's check
   command). Explain that for this tool, this is a settings file or a menu.

## Learner steps
1. Ask for the tool list.
2. Ask for one small task and read the breakdown.
3. Allowlist one safe action.

## Completion check
The learner can name three tools, and one safe action is allowlisted in their
tool's settings (or they can explain why their tool doesn't support that).

## Hints
1. Ask: "Where are your permission settings stored?"

## Takeaway
The model chooses, the tool program acts, and the result comes back into
context. Permission settings let you control that loop in advance instead of
approving each action.
