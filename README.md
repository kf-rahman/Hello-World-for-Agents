# Hello World for Agents

A self-paced, turn-based course on working with AI agents. You take it
**inside the agent you're learning to use**, and it takes about **2 hours**.

## Course learning goal

By the end, you can **hand off a real multi-step task to an AI agent and get a
verified result**. To do that, you write prompts that describe an outcome,
manage what the agent knows, extend it with skills and MCP, and choose the right
kind of agent tool for the job.

## Who it's for

The course adapts to two settings you choose at the start:

| | **Engineer** (works in code) | **Business** (works in documents, data, processes) |
|---|---|---|
| **Novice**: never used a coding agent | Full walkthrough, software project | Full walkthrough, business project, no jargon |
| **Adept**: used ChatGPT or Copilot chat, but not agents | Faster pace, software project | Faster pace, business project |

## How to start

1. **Clone the repo**
   ```bash
   git clone https://github.com/kf-rahman/Hello-World-for-Agents.git
   cd Hello-World-for-Agents
   ```
2. **Open an AI agent in this folder**: Claude Code, Codex, Gemini CLI,
   Cursor, GitHub Copilot agent mode, or similar. New to this? See
   [docs/SETUP.md](docs/SETUP.md).
3. **Type `start`.**

The agent reads [`AGENTS.md`](AGENTS.md) (Claude Code reads it through
[`CLAUDE.md`](CLAUDE.md)) and becomes your course guide. It gives you one step
at a time, checks your work, and saves your progress to `save/save.md`.

| Command | Effect |
|---------|--------|
| `start` | Begin or resume |
| `next` | Move on once the current exercise is complete |
| `hint` | Get a hint |
| `check` | Have the guide check your work |
| `status` | Progress and time used |
| `map` | All modules and exercises |
| `explain` | Explain the last step in more depth |

## Modules

| # | Module | Time | Learning goal |
|---|--------|------|---------------|
| 0 | [Getting Started](modules/00-getting-started/) | 10 min | Explain how an agent differs from a chatbot, approve or deny its actions safely, and build a practice project from your own recent work |
| 1 | [Prompting](modules/01-prompting/) | 25 min | Write prompts an agent can carry out without guessing: outcome, context, constraints, how to confirm it's done |
| 2 | [Context & Memory](modules/02-context-memory/) | 20 min | Control what the agent knows with memory files and fresh-session handoffs |
| 3 | [Tools & Skills](modules/03-tools-skills/) | 20 min | Understand how agents act through tools, and package a workflow as a skill |
| 4 | [MCP](modules/04-mcp/) | 15 min | Understand what MCP is, how it differs from an API, and when to use it, and then use one |
| 5 | [Agent Surfaces](modules/05-agent-surfaces/) | 10 min | Know why agents come as chat apps, IDE tools, CLIs, and cloud services, and pick the right one |
| 6 | [Capstone](modules/06-capstone/) | 20 min | Take one realistic task from spec to verified result, using everything above |

## Repository layout

```
AGENTS.md        Course guide instructions (read by most agents)
CLAUDE.md        Imports AGENTS.md for Claude Code
GEMINI.md        Imports AGENTS.md for Gemini CLI
modules/         One folder per module: README (goals and concepts) + exercises/
projects/        How the guide builds your practice project, plus example scenarios
workspace/       Your practice project (built in Module 0, not committed to git)
save/            Your progress file (not committed to git)
docs/            Setup guide, course design notes, presentation
```

## Contributing

Exercises are Markdown files in a fixed format. See
[docs/COURSE_DESIGN.md](docs/COURSE_DESIGN.md).
