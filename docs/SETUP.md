# Setup Guide

You need three things: **git**, **Python 3.9+** (for the playground), and **one
coding agent**. If you already have them, go back to the
[README](../README.md) and type `start`.

## 1. Install git and Python
- **macOS:** `xcode-select --install` installs git. Get Python from python.org or Homebrew.
- **Windows:** install [Git for Windows](https://git-scm.com/download/win) and
  Python from python.org (tick "Add to PATH"). WSL is recommended for terminal agents.
- **Linux:** use your package manager.

## 2. Pick a coding agent
Any tool that can read files and run commands in this folder will work. If you
don't know which one to pick, start with a terminal agent. The course is
written for them first.

| Tool | Type | Get started |
|------|------|-------------|
| Claude Code | Terminal (also IDE, desktop, web) | https://docs.claude.com/en/docs/claude-code |
| OpenAI Codex CLI | Terminal (also IDE, cloud) | https://developers.openai.com/codex |
| Gemini CLI | Terminal | https://github.com/google-gemini/gemini-cli |
| Cursor | IDE | https://cursor.com |
| GitHub Copilot (agent mode) | IDE | https://docs.github.com/copilot |

> Install steps and pricing change often, so follow each tool's official docs.
> Most need a paid plan or an API key.

## 3. Clone and start
```bash
git clone https://github.com/kf-rahman/Hello-World-for-Agents.git
cd Hello-World-for-Agents
claude   # or: codex, gemini, or open the folder in your IDE
```
Then type **`start`**.

## Troubleshooting
- **The agent doesn't act like a Game Master.** Your tool may not have loaded
  the instructions file. Say: *"Read AGENTS.md and follow it."*
- **Gemini CLI** reads `GEMINI.md`, which imports `AGENTS.md`.
- **Want to restart?** Type `reset`, or delete `save/save.md`.
