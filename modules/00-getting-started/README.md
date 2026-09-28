# Module 0: Getting Started

**Time:** 10 minutes

## Learning goal
The learner can explain how an AI **agent** differs from a chatbot, and can
safely approve or deny the actions it proposes. They leave with a practice
project built from their own recent work.

## Objectives
- Describe the agent loop: *read → plan → act → observe → repeat*.
- Name the three parts of an agent: **model, tools, context**.
- Recognize a permission request and decide whether to approve it.

## Key concepts

**Chatbot vs agent.** A chatbot gives an answer and stops. An agent works in a
loop: it takes an action (reads a file, runs a command, edits a document),
looks at the result, and decides what to do next, until the task is done or it
needs your input.

**Model, tools, context.**
- *Model*: the AI model that does the reasoning.
- *Tools*: the actions available to it (read and edit files, run commands,
  search, connect to other systems).
- *Context*: everything the model can see right now: your messages, files it
  has read, results from its tools, and instruction files like `AGENTS.md`.

**Permissions.** Agents take real actions, so they ask before risky ones.
Approving everything without reading is the most common beginner mistake.

## Persona notes
- **Engineer:** relate the loop to debugging: reproduce, inspect, change, rerun.
- **Business:** relate the loop to handing a task to a capable new colleague who
  checks in before doing anything that can't be undone.

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [Setup](exercises/01-setup.md) | 2 |
| 2 | [Build Your Project](exercises/02-build-your-project.md) | 5 |
| 3 | [Permissions](exercises/03-permissions.md) | 3 |
