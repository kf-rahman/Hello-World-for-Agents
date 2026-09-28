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

Give the learner the two `P0.1` requests from their project, **one at a
time**:

1. **Safe action (approve).** Do it through your normal tools so a real
   permission prompt can appear. Afterwards, ask whether a prompt appeared,
   and **wait for the answer** before going on.
2. **Destructive action (deny).**
   - If a prompt appeared for the safe action, attempt the destructive action
     normally so the learner can deny it at the prompt.
   - If **no prompt appeared**, the tool is probably approving actions
     automatically, and nothing would stop the delete. **Don't attempt it.**
     Explain that in this mode the file would simply be deleted, describe the
     prompt they'd see in an "ask first" mode, and suggest switching to that
     mode while they learn (point them to their tool's docs).
   - If the file is deleted anyway, restore it from `save/backup/` and explain
     what happened.

Then ask: *"When would you let an agent act without asking you first?"*

## Learner steps
1. Make the safe request and approve it. Tell the guide whether a prompt appeared.
2. Make the destructive request and deny it (or, if your tool approves actions
   automatically, hear why the guide won't attempt it).
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
