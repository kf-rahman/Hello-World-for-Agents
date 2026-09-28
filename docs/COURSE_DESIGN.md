# Course Design

Status: **content drafted for all modules. Practice projects not chosen yet.**

## Course learning goal
By the end, the learner can **hand off a real multi-step task to an AI agent and
get a verified result**. To do that, they write prompts that describe an
outcome, manage what the agent knows, extend it with skills and MCP, and choose
the right kind of agent tool for the job.

## Audience
Learners choose two settings at the start:

- **Experience:** `novice` (never used a coding agent) or `adept` (has used chat
  AI tools, but not agentic workflows). This controls pace, how much is
  explained, and which exercises can be skipped.
- **Persona:** `engineer` or `business`. This controls the practice project,
  the examples, and what "verified" means (tests passing vs outputs checked
  against their sources).

## How it works
There's no program to install. `AGENTS.md` makes the learner's own agent act as
the **course guide**, which:
- reads and updates `save/save.md` (progress),
- runs exercises from Markdown files,
- checks completion against real files, command output, or the conversation.

The course demonstrates its own concepts: `AGENTS.md` is a memory file,
`save/save.md` is external memory, and each exercise file is a structured
prompt. The guide points this out in Module 2.

## Time budget (2 hours)

| # | Module | Minutes | Exercises |
|---|--------|---------|-----------|
| 0 | Getting Started | 10 | 3 |
| 1 | Prompting | 25 | 3 |
| 2 | Context & Memory | 20 | 3 |
| 3 | Tools & Skills | 20 | 3 |
| 4 | MCP | 15 | 2 |
| 5 | Agent Surfaces | 10 | 2 |
| 6 | Capstone | 20 | 1 |
| | **Total** | **120** | **17** |

Novices will probably run over on Modules 1 to 3. Adepts can skip the exercises
marked `skippable: true` (about 30 minutes' worth), which leaves room for that.

## Projects
Exercises are written without reference to a project and point to **task
slots** (`P0.1` … `P6.1`). Each persona's project fills those slots. See
[projects/README.md](../projects/README.md) for the requirements. Both projects
are **to be decided**.

## Module 4 (MCP) approach
The focus is the mental model, not building a server: what MCP is, how it
differs from an API (and why it isn't "MCP instead of an API"), when to use a
built-in tool, a skill, or MCP, and security. Then the learner connects one
server and uses it.

## Module 5 (Agent Surfaces) approach
The focus is on *why* different forms exist (chat and desktop apps, IDE,
terminal, web/cloud, automation), using Claude Code, Codex, and Copilot as
examples. It is not a feature-by-feature product comparison. Product details
change quickly, so the content avoids specific version claims, and the guide is
told to check official docs.

## Open questions
1. **Projects:** choose the engineer and business projects, and fill in the slots.
2. **Business setup:** which tool should business learners use by default?
   The course needs an agent that can read and write files in the repo (a
   desktop app, an IDE, or a CLI).
3. **Module 4 server:** pick one default MCP server that needs no account or
   API key for each persona.
4. **Deterministic checks:** add check scripts to each project, or rely on
   the guide's judgment?
5. **Live vs self-paced:** will the presentation be given alongside a live run
   of the course?
