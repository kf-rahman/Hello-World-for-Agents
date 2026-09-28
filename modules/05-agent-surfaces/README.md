# Module 5: Agent Surfaces

**Time:** 10 minutes

## Learning goal
The learner knows the **different ways AI agents are offered** (chat apps, IDE,
terminal, web/cloud, and automation), understands *why* each exists, and can
pick the right one for a task.

## Objectives
- Name the main surfaces and one example of each.
- Explain why a single product (for example Claude Code, Codex, or Copilot) is
  offered in several surfaces.
- Pick a surface for a task based on where you work, where the agent runs, and
  how closely you want to supervise it.

## Key concepts

**Same agent, different surfaces.** The agent loop, prompting, memory files,
skills, and MCP from Modules 1 to 4 work much the same everywhere. What
changes is **where the agent runs**, **how you interact with it**, and **what
it can reach**.

| Surface | Examples | Where it runs | Best when |
|---------|----------|---------------|-----------|
| **Chat & desktop apps** | Claude app, ChatGPT, Microsoft Copilot | Vendor's cloud, plus connectors | Thinking, drafting, analysis, working with documents; easy starting point for non-engineers |
| **IDE** | GitHub Copilot in VS Code/JetBrains, Cursor, Claude Code and Codex IDE extensions | Your machine, inside the editor | You want to see every change as a diff and stay close to the code |
| **Terminal (CLI)** | Claude Code, Codex CLI, Gemini CLI, Copilot CLI | Your machine | Full access to your environment, works with any editor, can be scripted |
| **Web / cloud (asynchronous)** | Claude Code on the web, Codex cloud, Copilot coding agent on GitHub | A remote sandbox | Handing off tasks, running several in parallel, working from a phone; results come back as a branch or PR |
| **Automation** | GitHub Actions integrations, agent SDKs | CI or your own servers | Triggered by events (a new issue or PR, a schedule), with no human in the loop |

*(Products and features change quickly. The guide should confirm details
against official docs before stating them as current.)*

**Why so many surfaces?** Each one answers a different question:
- *Where do you already work?* Editor → IDE; terminal → CLI; browser or
  documents → chat or desktop app.
- *Where should the agent run?* Locally, with access to your files and tools,
  or in a cloud sandbox that is isolated and keeps running when you close the
  laptop.
- *How involved do you want to be?* Working alongside it step by step
  (IDE, CLI), or handing off the task and reviewing the result later
  (web/cloud, automation).

**Where the major products started.** GitHub Copilot started as code
autocomplete in the IDE, added chat and then an agent mode, and now also offers
a cloud agent you can assign GitHub issues to. It lets you choose between
models from several providers. Claude Code and Codex started as terminal
agents, then expanded into IDE extensions, desktop apps, and cloud/web versions.
They are converging from different starting points.

## Persona notes
- **Engineer:** focus on IDE vs CLI vs cloud, and when to delegate work
  asynchronously (well-defined tasks with clear verification).
- **Business:** focus on chat and desktop apps with connectors, and on how
  "coding" agents are increasingly used for non-code work (documents, data,
  reports).

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [Surface Tour](exercises/01-surface-tour.md) | 5 |
| 2 | [Pick the Surface](exercises/02-pick-the-surface.md) | 5 |
