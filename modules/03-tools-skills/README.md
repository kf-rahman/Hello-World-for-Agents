# Module 3: Tools & Skills

**Time:** 20 minutes

## Learning goal
The learner understands how an agent **acts through tools** and can package a
repeated workflow as a **skill** that the agent picks up on its own when it's
relevant.

## Objectives
- Explain a tool call: the model requests it, the tool program carries it out,
  and the result goes back into the context.
- Name the common built-in tools: read and search, edit, run commands, web, and
  delegating to sub-agents.
- Explain how permission settings (allowlists, deny rules, modes) control tools.
- Write a skill, and tell it apart from a memory file, a custom command, and a
  hook.

## Key concepts

**A tool is a function with a description.** The model reads each tool's
description to decide when to use it. The tool program (Claude Code, Codex,
Cursor, and so on) runs the tool and returns the result to the model. The model
never runs anything directly.

**Permissions are settings.** Beyond yes/no prompts, most tools let you
allowlist safe actions ("always allow running tests"), deny dangerous ones, or
switch modes (read-only, ask every time, auto-approve). Set these up on purpose.

**Skills.** A skill is a folder containing a `SKILL.md` file (instructions,
plus optional scripts and templates). The agent sees only each skill's short
description until a task matches it; then it loads the full instructions. That
keeps the context small. The `SKILL.md` format started in Claude Code and is now
supported by several other tools. *(Check your tool's docs for current support
and the folder it reads skills from.)*

**How the pieces differ:**

| Feature | Loaded | Use it for |
|---------|--------|------------|
| Memory file | Always | Facts about this project |
| Skill | When relevant | A repeatable procedure or area of know-how |
| Custom command | When you type it | A shortcut you run on purpose |
| Hook | Automatically, on an event | Rules that must always run (for example, formatting after every edit) |

## Persona notes
- **Engineer:** a release checklist, a code-review procedure, or scaffolding a
  new endpoint.
- **Business:** a weekly report, turning meeting notes into action items, or
  applying the brand style to a document.

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [Inspect the Tools](exercises/01-inspect-tools.md) | 5 |
| 2 | [Write a Skill](exercises/02-write-a-skill.md) | 10 |
| 3 | [Checkpoint: The Skill Gets Used](exercises/03-checkpoint-skill.md) | 5 |
