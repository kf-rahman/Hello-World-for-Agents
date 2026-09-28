---
id: 3.2
title: Write a Skill
minutes: 10
skippable: false
demo: false
project_slot: P3.1
---

## Purpose
Package the `P3.1` workflow as a skill.

## Guide instructions
1. Explain the `P3.1` workflow and why it's a good candidate: it's repeated,
   has several steps, and is easy to get wrong.
2. Tell the learner where their tool loads skills from (for example, Claude
   Code uses `.claude/skills/<name>/SKILL.md`). If their tool doesn't support
   skills, use a custom command or a section in the memory file instead, and
   explain the difference.
3. Explain the structure of a `SKILL.md` file:
   ```markdown
   ---
   name: weekly-report
   description: Use when the user asks for the weekly report or a status summary.
   ---
   # Steps
   1. ...
   ```
   Stress that **the description decides when the skill is used**. It's a
   prompt, so write it as one.
4. The learner writes the skill. Review it, but don't write it for them.

## Learner steps
1. Create the skill folder and `SKILL.md`.
2. Write a description that says when to use it.
3. Write the steps, including how to verify the result.

## Completion check
- A `SKILL.md` exists in the tool's skill folder, with a `name`, a specific
  `description` that says when to use it, and numbered steps.
- The steps include a verification step.

## Hints
1. The description should name the situations or phrases that should trigger it.
2. Write the steps as you would for a new colleague: specific, in order,
   and checkable.

## Takeaway
A skill turns something you'd otherwise explain every time into something the
agent already knows how to do, and it loads only when needed.
