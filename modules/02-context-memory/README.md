# Module 2: Context & Memory

> *The tavern's old scribe taps his head. "An agent remembers nothing between
> visits, unless you write it down."*

## Learning objectives
- Explain the **context window**: the agent's working memory, which is limited
  and fills up.
- Know what fills it (messages, file reads, tool output) and what happens when
  it's full (compaction, or forgetting).
- Write a **project memory file** (`AGENTS.md` / `CLAUDE.md`) that makes every
  future session better.
- Know when to **start fresh** versus continue, and how to hand off with a
  notes file.

## Key ideas (draft)
- **Stateless by default.** Each new session starts blank. This course's
  `AGENTS.md` and `save/save.md` are working examples of memory files. Point
  that out to the player.
- **Memory hierarchy.** User-level vs project-level vs folder-level memory files.
  The file names differ by tool (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor
  rules), and the idea is the same everywhere.
- **Context rot.** Long sessions full of dead ends make agents worse. Fresh
  context plus a good handoff note usually beats one huge session.
- **What belongs in memory:** how to build and test, conventions, gotchas.
  **What doesn't:** things the agent can read from the code itself.

## Planned quests
| # | Quest | Summary |
|---|-------|---------|
| 1 | Goldfish | Start a *new* session and ask about the last fix. See that the agent doesn't remember. |
| 2 | The Scribe's Ledger | Write `playground/AGENTS.md` (run command, test command, conventions). Check it in a fresh session. |
| 3 | Too Much Noise | Pollute the context (huge output, off-topic tangents), see answers get worse, then compact or restart. |
| 4 | BOSS: The Handoff | Stop mid-task, write a handoff note, and have a *fresh* session finish the job using only the note. |

**Checkable win conditions:** memory file exists with specific facts; a fresh
session answers "how do I run the tests?" correctly without searching.
