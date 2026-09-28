---
id: 00-01
title: Hello, Agent
xp: 100
skippable: false
demo: true
---

## Briefing
Welcome the player to *Hello World for Agents*. Explain in two or three sentences:
- You (the agent) are both their guide and the thing they're learning about.
- The game is turn-based. They type a command, you take one step, and you wait.
- Their progress lives in `save/save.md`, a plain file you'll update as they go.

Then ask two questions, one at a time:
1. What should I call you?
2. Which describes you best?
   - **[1] Novice**: never used a coding agent
   - **[2] Adept**: have used ChatGPT, Copilot, or similar chat tools, but not agents

Also ask which tool they're playing in (Claude Code, Codex, Cursor, and so on).
If they don't know, work it out from your own identity and confirm with them.

## Tasks
1. Player answers the questions.
2. GM (demo) creates `save/save.md` from `save/save.template.md` and fills in
   `name`, `track`, `agent_tool`, and `started` (today's date).
3. GM shows the player the file it just wrote and points out: *"I just used a
   tool to write a file. A chatbot couldn't do that."*

## Win condition
`save/save.md` exists with `name`, `track` (`novice` or `adept`), and
`agent_tool` filled in.

## Hints
1. Just answer the GM's questions. There's nothing to code yet.
2. If the save file wasn't created, ask the GM: "please create my save file."

## Debrief
That file you just watched being written is the whole idea of this course in
miniature: **an agent is a model that can take actions**. Type `next`.
