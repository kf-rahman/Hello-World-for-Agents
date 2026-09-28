---
id: 0.3
title: Permissions
minutes: 3
skippable: true
demo: false
project_slot: P0.1
---

## Purpose
Practice being the approver: allow a safe action and refuse a destructive one.

## Guide instructions
Explain that agents ask before actions that change things or reach outside the
computer. Tools handle this differently (prompts, modes, allowlists, sandboxes),
but in every case the learner is the approver.

Before starting, **copy the key input file named in `P0.1` to `save/backup/`**
so it can be restored.

Give the learner the two `P0.1` requests from their project: one safe action to
**approve** and one destructive action to **deny**. Attempt both through your
normal tools so that real permission prompts appear. If your tool is in a mode
that approves actions automatically, say so and describe the prompt they would
normally see. If they approve the destructive action by mistake, restore the
file from `save/backup/` and explain what happened.

Then ask: *"When would you let an agent act without asking you first?"*

## Learner steps
1. Make the safe request and approve it.
2. Make the destructive request and deny it.
3. Answer the question.

## Completion check
- The key input file still exists in `workspace/`.
- The learner answered the question.

## Hints
1. Look for the approve/deny prompt in your tool's interface.
2. For the question, compare actions that are low risk and easy to undo with
   ones that can't be undone.

## Takeaway
Permissions trade speed for safety. Approve step by step at first. Give the
agent more freedom as your trust grows and when you have a safety net, such
as version control or backups.
