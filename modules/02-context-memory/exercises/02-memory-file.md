---
id: 2.2
title: Write a Memory File
minutes: 8
skippable: false
demo: false
project_slot: P2.1
---

## Purpose
Write a project memory file and confirm that a new session uses it.

## Guide instructions
Explain which memory file name their tool uses (see the module README). Ask the
learner to create `workspace/AGENTS.md` (plus a `workspace/CLAUDE.md` containing
`@AGENTS.md` if they're using Claude Code) with the `P2.1` facts from their
project. Coach them to keep it short, specific, and useful.

Then have them test it: in a **new session**, ask a question the memory file
answers (for example, "How do I check that my changes are correct in this
project?") and see whether the agent answers without searching.

## Learner steps
1. Write the memory file.
2. Test it in a new session.
3. Make one improvement based on the test.

## Completion check
- `workspace/AGENTS.md` exists and contains the `P2.1` facts: how to run and
  check the project, plus at least one convention or known issue.
- The learner reports that a new session used it.

## Hints
1. Ask yourself what a new teammate would need to know on day one.
2. Leave out anything the agent could learn by reading one file.
3. Use short bullet points, not paragraphs.

## Takeaway
A memory file is how you tell the agent "every time you work here, know this."
It pays off in every future session.
