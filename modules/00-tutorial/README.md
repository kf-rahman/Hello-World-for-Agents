# Module 0: Tutorial, Hello Agent

> *You wake in a tavern. The barkeep slides a scroll across the counter:
> "Heard you're here to learn the ways of the agent."*

## Learning objectives
- Tell a **chatbot** (answers questions) apart from an **agent** (takes actions
  in a loop).
- Name the three parts of an agent: **model + tools + context**.
- Watch the agent loop happen live: *read → plan → act → observe → repeat*.
- Approve or deny a permission request, and know why the request exists.

## Key ideas (GM: teach these, pitched to the player's track)

**The agent loop.** A chat model gives one answer and stops. An agent runs in a
loop. It decides on an action, like reading a file or running a command, sees
the result, and decides what to do next. It stops when the task is done or it
needs you.

**Model + tools + context.**
- *Model*: the LLM doing the thinking.
- *Tools*: what it can do (read files, edit, run shell commands, search the web).
- *Context*: everything it can "see" right now: your messages, files it has
  read, tool results, and memory files like `AGENTS.md`.

**Permissions.** Because agents act, they ask before risky actions. Approving
blindly is the most common beginner mistake.

## Quests
| # | Quest | Summary |
|---|-------|---------|
| 1 | [Hello, Agent](quests/01-hello-agent.md) | Character creation: pick a track, create the save file |
| 2 | [Watch the Loop](quests/02-watch-the-loop.md) | Ask the agent to explore the playground and narrate its loop |
| 3 | [Mind the Gate](quests/03-mind-the-gate.md) | Meet permissions: approve one action, deny one, and see what happens |
