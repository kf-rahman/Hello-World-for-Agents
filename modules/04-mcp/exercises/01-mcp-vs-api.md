---
id: 4.1
title: MCP vs API
minutes: 7
skippable: false
demo: false
project_slot: none
---

## Purpose
Build a clear mental model of MCP before using it.

## Guide instructions
1. Teach the key concepts from the module README, briefly, at the learner's level.
2. Give the learner these six scenarios, and ask them to say for each one whether
   it calls for a **built-in tool**, a **skill**, or **MCP**, with a short reason:
   1. Read a document in the current folder.
   2. Look up open tickets in the company's issue tracker.
   3. Always format reports the way the finance team expects.
   4. Query the production customer database.
   5. Follow the team's 6-step release checklist.
   6. Post a summary to a team chat channel.
3. Then ask: *"A service already has a public API. Why would anyone build an MCP
   server for it?"*
4. Give feedback on their answers. Suggested answers: 1 built-in, 2 MCP, 3
   skill, 4 MCP, 5 skill, 6 MCP. Accept other answers that are well reasoned.

## Learner steps
1. Classify the six scenarios.
2. Answer the API question.

## Completion check
At least five of the six scenarios are reasonably classified, and the answer to
the API question mentions at least one of: a standard format across services,
the AI discovering tools at run time, or build once and use in any client.

## Hints
1. Ask: is this *know-how* (skill) or *access to a system* (MCP)?
2. For the API question: think about the work of connecting one AI app to 50
   different APIs, compared with connecting it to 50 servers that all follow
   one standard.

## Takeaway
An API is how a system is reached; MCP makes that system usable by any AI agent
in a standard way. Skills are know-how, and MCP is access.
