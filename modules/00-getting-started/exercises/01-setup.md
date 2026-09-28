---
id: 0.1
title: Setup
minutes: 2
skippable: false
demo: true
project_slot: none
---

## Purpose
Record who the learner is so the course can adapt, and give the first example of
an agent taking an action.

## Guide instructions
1. In two or three sentences, explain the course: it's turn-based, the learner
   types a command and you take one step, and progress is saved in
   `save/save.md`. Mention the commands `start`, `next`, `hint`, `check`,
   `status`.
2. Ask, one at a time:
   - What name should I use for you?
   - Experience: **[1] Novice**, never used a coding agent; **[2] Adept**, used
     chat AI tools such as ChatGPT or Copilot chat, but not agents.
   - Persona: **[1] Engineer**, you work in code; **[2] Business**, you work
     mainly with documents, data, and processes.
   - Which tool are you using right now? If they aren't sure, work it out and
     confirm with them.
3. (Demo) Create `save/save.md` from the template and fill in the answers.
4. Point out: *"I just created and edited a file. A chatbot can only reply with
   text; an agent can take actions."*

## Learner steps
1. Answer the questions.

## Completion check
`save/save.md` exists with `name`, `experience`, `persona`, and `agent_tool`
filled in.

## Hints
1. Just answer the questions. There's nothing to build yet.

## Takeaway
An agent is a model that can take actions. You just saw it write a file.
