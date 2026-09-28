---
id: 4.2
title: Connect and Use a Server
minutes: 8
skippable: false
demo: false
project_slot: P4.1
---

## Purpose
Connect a real MCP server that helps with everyday work, use it on the
learner's project, and look at what it gives the agent.

## Guide instructions
1. **Pick the server by persona** (details in the module README):
   - **Business: PowerPoint.** Any reasonably maintained PowerPoint MCP server
     that creates `.pptx` files will do; help the learner pick one quickly.
     The task: turn the project's findings into a short slide deck (`P4.1`).
   - **Engineer: Excalidraw.** The task: diagram how the project works, for its
     documentation (`P4.1`).
2. **Vet before connecting.** Ask the learner who publishes the server, what it
   can access, and whether it runs locally or remotely. For PowerPoint, the
   servers are community-built, so treat this as a real check: read the
   project's README and tool list first.
3. **Help the learner add it** using their tool's method (a command, a settings
   file, or a connectors menu). Look up the current method in the tool's docs
   rather than relying on memory.
4. The learner asks you to list the server's tools and read one tool's
   description.
5. The learner gives you the `P4.1` request, and you use the server to do it.
6. Ask: *"What could go wrong if this server were malicious or had too much
   access?"
7. **Business learners:** remind them the deck is a first draft. They can move
   it to SharePoint (or wherever they keep files) and edit it like any other
   deck.*

## Learner steps
1. Check who publishes the server and what it can access.
2. Add the server.
3. Look at its tools.
4. Use it on the `P4.1` task.
5. Name one risk.

## Completion check
- The server appears in the tool's MCP or connector list.
- The agent used one of its tools to produce the `P4.1` output: a `.pptx` file
  in `workspace/` for business, or an Excalidraw diagram for engineers.
- The learner named a specific risk.

## Hints
1. Ask the agent: "How do I add an MCP server in this tool?"
2. Excalidraw not displaying? Your tool may not support showing interactive MCP
   content. Ask for a link or an exported file instead.
3. Risks to consider: the data it can see, the actions it can take, and
   instructions hidden in tool descriptions or in the data it returns.

## Takeaway
You just gave the agent a new ability that you'll use again: making slides or
diagrams from your work. Treat every server like any other access you grant:
understand it, limit it, and trust its source.
