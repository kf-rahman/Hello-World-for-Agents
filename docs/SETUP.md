# Setup Guide

You need **git** and **one AI agent that can read and edit files in a folder**.
Your practice project may need one more tool; the course guide will tell you.
If you already have these, go back to the [README](../README.md) and type
`start`.

## 1. Install git
- **macOS:** run `xcode-select --install` in Terminal.
- **Windows:** install [Git for Windows](https://git-scm.com/download/win).
- **Linux:** use your package manager.

Prefer not to use the command line? GitHub Desktop can clone the repo for you.

## 2. Choose an agent
Any agent that can open this folder, read files, and run commands will work.

| Tool | Surface | Good first choice for |
|------|---------|-----------------------|
| Claude Code | Terminal, IDE extension, desktop app, web | Engineers; business users via the desktop app |
| OpenAI Codex | Terminal, IDE extension, desktop app, cloud | Engineers |
| GitHub Copilot (agent mode) | VS Code, JetBrains | Engineers already using VS Code |
| Cursor | IDE | Engineers who want an AI-first editor |
| Gemini CLI | Terminal | Engineers |

Official docs:
- Claude Code: https://docs.claude.com/en/docs/claude-code
- Codex: https://developers.openai.com/codex
- GitHub Copilot: https://docs.github.com/copilot
- Cursor: https://cursor.com/docs
- Gemini CLI: https://github.com/google-gemini/gemini-cli

> Installation steps, plans, and pricing change often, so follow the official
> docs. Most of these tools need a paid plan or an API key.

## 3. Clone and start
```bash
git clone https://github.com/kf-rahman/Hello-World-for-Agents.git
cd Hello-World-for-Agents
```
Open your agent in that folder, then type **`start`**.

## Troubleshooting
- **The agent doesn't act as a course guide.** It may not have loaded the
  instructions. Say: *"Read AGENTS.md and follow it."*
- **Start over.** Type `reset`, or delete `save/save.md`.
