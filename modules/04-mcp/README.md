# Module 4: MCP (Model Context Protocol)

> *A traveling merchant opens a case of adapters. "Every kingdom has its own
> plug. This one fits them all."*

## Learning objectives
- Explain MCP simply: a **standard plug** that lets any agent use outside tools
  and data (GitHub, databases, docs, browsers, Slack, and so on).
- Tell MCP apart from built-in tools and from skills.
- Add an MCP server to an agent and use it.
- Understand the **security model**: MCP servers run code and see data, so only
  install ones you trust, and give them the least access they need.
- (Stretch) Build a tiny MCP server that exposes the Tavern Ledger.

## Key ideas (draft)
- **Client / server.** The agent is the client. An MCP server exposes
  *tools* (actions), *resources* (data), and *prompts* (templates).
- **Local (stdio) vs remote (HTTP) servers.**
- **When to use which:** skill = know-how, MCP = access to a system.
- **Context cost.** Every connected server's tool descriptions use up context,
  so connect what you need, not everything.

## Planned quests
| # | Quest | Summary |
|---|-------|---------|
| 1 | The Universal Plug | Concept check: sort ten scenarios into built-in tool, skill, or MCP |
| 2 | Hire a Merchant | Install a harmless, well-known MCP server (for example a docs or fetch server) and use it |
| 3 | Read the Contract | Look at the server's tool list and descriptions, and name one risk |
| 4 | BOSS: Build the Ledger Server | Build a small MCP server (Python, official SDK) exposing `list_stock` and `sell`, then connect it and use it from the agent |

**Open question:** quest 4 needs `pip install`. Make it optional for novices?
