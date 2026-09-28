# Course Design

Status: **content drafted for all modules. Not yet tested in a real agent session.**

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

## Projects: built from the learner's own work
There's no fixed practice project. In Module 0, the guide asks the learner
about **one piece of work from the last two weeks** and generates a small
project modelled on it, with synthetic data and planted issues. The spec is
[projects/README.md](../projects/README.md). Anyone who can't think of
something, or wants to move faster, can pick a scenario from
[projects/examples.md](../projects/examples.md).

Why:
- Every learner practices on something that looks like their real job, so the
  results carry straight over to their work.
- Watching the agent build the project is the agent-loop demo.
- Describing their own work to the agent is an early prompting exercise.

How it stays consistent and checkable:
- Exercises use **task slots** (`P0.1` … `P6.1`). The generated
  `save/project-key.md` fills every slot, so the exercises never depend on a
  particular project.
- Every project must include a way to verify work: **tests** (engineer) or
  **`CHECKS.md` checks against the source data** (business).
- **Confidentiality:** the guide asks for the *kind* of work only and never
  writes real client names, figures, or documents into files. All data is
  synthetic. `workspace/` is not committed to git.

Risks to watch in testing: how much projects vary between agents and models,
and whether building the project fits in 5 minutes.

## Module 4 (MCP) approach
The focus is the mental model, not building a server: what MCP is, how it
differs from an API (and why it isn't "MCP instead of an API"), when to use a
built-in tool, a skill, or MCP, and security. Then the learner connects a real
server for their daily work, **PowerPoint** (business) or **Excalidraw**
(engineer), and uses it on their project.

## Module 5 (Agent Surfaces) approach
The focus is on *why* different forms exist (chat and desktop apps, IDE,
terminal, web/cloud, automation), using Claude Code, Codex, and Copilot as
examples. It is not a feature-by-feature product comparison. Product details
change quickly, so the content avoids specific version claims, and the guide is
told to check official docs.

## Open questions
1. **Module 4 PowerPoint server:** choose which community PowerPoint MCP
   server to recommend (after vetting), or let the guide help each learner
   choose.
2. **Playtest:** run the course in at least two agents, one for each persona,
   to check timing and consistency, especially for building the project.
3. **Live vs self-paced:** will the course be run live after the leadership
   presentation, or only self-paced?

**Decided:** the course doesn't depend on which tool the learner uses; there's
no default tool for business learners. Projects are generated from the
learner's own recent work.
