# Module 4: MCP (Model Context Protocol)

**Time:** 15 minutes

## Learning goal
The learner understands **what MCP is, how it differs from an API, and when to
use it**. They leave with one real MCP server connected that helps with their
daily work: **PowerPoint** for business, **Excalidraw** for engineers.

## Objectives
- Explain MCP in one sentence.
- Explain how MCP relates to an API, and why "MCP vs API" is a false choice.
- Decide whether a need calls for a built-in tool, a skill, or MCP.
- Vet, add, and use an MCP server on their own project, and name one risk.

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

## The servers used in this module

| Persona | Server | Everyday problem it solves | Notes |
|---------|--------|----------------------------|-------|
| **Business** | A **PowerPoint** MCP server | Turning analysis into slides | There's no official Microsoft server for this; the options are community-built, some creating `.pptx` files directly and some controlling the PowerPoint app. That makes it a good chance to practice **vetting a server**. If the firm uses Google Workspace, Google publishes an official **Google Slides** MCP server. |
| **Engineer** | The official **Excalidraw** MCP server (`excalidraw/excalidraw-mcp`) | Diagrams for documentation: architecture, flows, sequences | A remote server with nothing to install and no account. Interactive diagrams display only in tools that support showing MCP content inline (for example Claude, ChatGPT, VS Code); others may need an exported file. |

*(Check the current install steps and support in each server's docs before
running the module.)*

## Persona notes
- **Business:** relate MCP to systems they already use. **Salesforce** now
  offers official hosted MCP servers (generally available since April 2026), so
  the same idea can connect an agent to the firm's CRM, with IT approval. Many
  chat and desktop apps offer ready-made **connectors**; those are MCP servers
  set up for you.
- **Engineer:** other examples include GitHub, databases, error monitoring,
  and library docs. Building an MCP server is a small project using an official
  SDK (not part of this course).

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [MCP vs API](exercises/01-mcp-vs-api.md) | 7 |
| 2 | [Connect and Use a Server](exercises/02-use-a-server.md) | 8 |
