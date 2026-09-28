# Hello World for Agents

A self-guided, turn-based course on working with AI coding agents.
You play it inside the agent you're learning about.

```
  ┌─────────────────────────────────────────────┐
  │  > start                                    │
  │                                             │
  │  GM: Welcome, traveler. Before we begin,    │
  │  have you used a coding agent before?       │
  │                                             │
  │    [1] Never. What's a coding agent?        │
  │    [2] I've used ChatGPT, but not agents    │
  └─────────────────────────────────────────────┘
```

## Who this is for

- **Novices**: you have never used a coding agent like Claude Code, Codex,
  Cursor, or Gemini CLI.
- **Adepts**: you have used chat AI tools like ChatGPT or Copilot chat, but you
  don't know how to get started with *agentic* workflows, where the AI reads
  files, runs commands, and makes changes itself.

## How to play

1. **Clone the repo**
   ```bash
   git clone https://github.com/kf-rahman/Hello-World-for-Agents.git
   cd Hello-World-for-Agents
   ```
2. **Open your coding agent in this folder.** Any of these work:
   ```bash
   claude        # Claude Code
   codex         # OpenAI Codex CLI
   gemini        # Gemini CLI
   ```
   Or open the folder in Cursor, Windsurf, or VS Code with Copilot agent mode.
   New to all of this? See [docs/SETUP.md](docs/SETUP.md).
3. **Type `start`.**

The agent reads [`AGENTS.md`](AGENTS.md) (or [`CLAUDE.md`](CLAUDE.md) /
[`GEMINI.md`](GEMINI.md)), which turns it into your Game Master. Your progress
is saved in `save/save.md`.

### Commands

| Command   | Effect |
|-----------|--------|
| `start`   | Begin or resume |
| `next`    | Move on once the current quest is complete |
| `hint`    | Get a nudge |
| `check`   | Have the GM verify your work |
| `status`  | Show XP and progress |
| `map`     | Show every module and quest |
| `explain` | Go deeper on what just happened |

## The world map

| # | Module | You'll learn to... |
|---|--------|--------------------|
| 0 | **Tutorial: Hello, Agent** | See how an agent differs from a chatbot: the loop of reading, acting, and checking |
| 1 | **Prompting** | Write task prompts that agents can act on: goals, constraints, and a definition of done |
| 2 | **Context & Memory** | Manage what the agent knows: memory files, context windows, compaction, and fresh starts |
| 3 | **Tools & Skills** | Understand tool calls and permissions, and write your own reusable skill |
| 4 | **MCP** | Connect an agent to outside systems with the Model Context Protocol |
| 5 | **The Tool Landscape** | Compare Claude Code, Codex, Gemini CLI, Cursor, Copilot, and others, and pick the right one for a job |
| 6 | **Final Boss** | Put it all together on one real task, from start to finish |

## Repo layout

```
AGENTS.md          # Game Master rules (read by most agents)
CLAUDE.md          # Imports AGENTS.md for Claude Code
GEMINI.md          # Imports AGENTS.md for Gemini CLI
save/              # Your save file (git-ignored)
modules/           # Lessons and quests, one folder per module
playground/        # The sandbox project you'll work on
docs/              # Setup guide, course design notes, presentation outline
```

## Contributing

Quests are plain Markdown with a fixed format. See
[docs/COURSE_DESIGN.md](docs/COURSE_DESIGN.md) for how they work and what's
planned.
