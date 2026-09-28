# Module 4: MCP (Model Context Protocol)

**Time:** 15 minutes

## Learning goal
The learner understands **what MCP is, how it differs from an API, and when to
use it**. They connect one MCP server and use it.

## Objectives
- Explain MCP in one sentence.
- Explain how MCP relates to an API, and why "MCP vs API" is a false choice.
- Decide whether a need calls for a built-in tool, a skill, or MCP.
- Add an MCP server to their tool, use it, and name one risk.

## Key concepts

**One sentence:** MCP is an open standard that lets any AI application connect
to outside tools and data in the same way, much as USB-C lets any device use the
same cable.

**How MCP differs from an API**

| | API | MCP |
|---|-----|-----|
| Written for | Developers writing code | AI applications and the models inside them |
| Shape | Different for every service (endpoints, authentication, formats) | The same for every server: tools, resources, prompts |
| How it's found | A developer reads the docs and writes code | The agent asks the server what it offers, at run time |
| Integration work | Each app writes code for each API | Build a server once, and it works in any MCP client |

**MCP is not a replacement for APIs.** Most MCP servers *wrap* an API. The API
is how the system is reached. MCP is the layer that makes it ready for an AI:
it describes the available actions in plain language so the model knows when
and how to use them.

**The pieces:**
- **Client (host):** the AI app you use (Claude Code, Codex, Cursor, a chat app).
- **Server:** a small program that offers:
  - *tools*: actions the agent can take
  - *resources*: data the agent can read
  - *prompts*: reusable templates
- **Local vs remote:** local servers run on your machine; remote servers are
  web services you sign in to.

**Built-in tool, skill, or MCP?**
- **Built-in tool:** what the agent can already do (files, shell, web).
- **Skill:** *know-how*, meaning how to do something.
- **MCP:** *access*, meaning a connection to a system the agent couldn't
  otherwise reach (your issue tracker, database, CRM, drive).

**Security.** A server can run code and see your data, and its tool
descriptions go straight into the model's context. Install only servers you
trust, give them the least access they need, and connect only what the task
requires. Every connected server also uses up context.

## Persona notes
- **Engineer:** examples include GitHub, a database, error monitoring, and
  library docs. Mention that building an MCP server is a small project using an
  official SDK (not part of this course).
- **Business:** examples include Google Drive, Slack, a CRM, and a calendar.
  Many chat and desktop apps offer these as ready-made **connectors**; those are
  MCP servers set up for you.

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [MCP vs API](exercises/01-mcp-vs-api.md) | 7 |
| 2 | [Connect and Use a Server](exercises/02-use-a-server.md) | 8 |
