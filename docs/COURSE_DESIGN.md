# Course Design (working doc)

Status: **first draft, open for feedback.** Modules 0 and 1 can be played now.
Modules 2 to 6 are outlines.

## Goals
1. Someone who has **never used a coding agent** can go from zero to
   confidently directing one.
2. Someone who **uses chat AI** (ChatGPT, Copilot chat) learns what changes when
   the AI can *act*, and builds working habits for agentic workflows.
3. **Tool-agnostic.** It works in Claude Code, Codex, Gemini CLI, Cursor, and
   others. Concepts first, brands second.

## Core mechanic: the agent is the game engine
There's no game code. `AGENTS.md` turns whatever agent the player opens into a
**Game Master** that:
- reads and writes `save/save.md` (state),
- runs quests from Markdown files (content),
- checks win conditions against real files and test runs (verification).

This works on two levels: **the way the course runs teaches the course.** The
save file *is* external memory (Module 2). `AGENTS.md` *is* a memory file
(Module 2). Quest files *are* structured prompts (Module 1). A later version
could package the GM as a skill (Module 3). We point this out as players go.

### Why not a Python CLI game?
We considered a `python play.py` engine. We chose the agent-as-GM approach
because:
- players practice with the real tool from the first minute,
- there's nothing to install beyond the agent,
- content is plain Markdown, so it's easy to contribute to.

Trade-off: the agent's behavior varies a bit between tools and models. Win
conditions rely on **checkable artifacts** (files, tests passing) so grading
stays mostly deterministic. We could add a `scripts/check.py` later to make
checks fully deterministic.

## Two tracks
| | Novice | Adept |
|--|--------|-------|
| Pace | One concept per turn, analogies | Faster, skip warm-ups |
| Module 0 | Full | Quests 2 and 3 skippable |
| Framing | "What is an agent?" | "What changes when the AI can act?" |

## Shared sandbox: the Tavern Ledger
`playground/tavern.py` is a tiny inventory CLI with bugs planted on purpose:
- `sell` on an unknown item → `KeyError` (Module 1, quest 1)
- overselling → negative stock (Module 1, quest 2)
- no `low` command (Module 1 boss)
- float money, no input validation (spare material for later modules)

One project across all modules means the player's context (and memory file)
builds up over time, which matches real work.

## Module map
| # | Module | Status | Boss |
|---|--------|--------|------|
| 0 | Tutorial | ✅ playable | — |
| 1 | Prompting | ✅ playable | One-shot prompt that ships and verifies a feature |
| 2 | Context & Memory | 📝 outline | Fresh-session handoff |
| 3 | Tools & Skills | 📝 outline | Skill gets used without being named |
| 4 | MCP | 📝 outline | Build a Tavern Ledger MCP server |
| 5 | Tool Landscape | 📝 outline | Tool-choice scenarios |
| 6 | Final Boss | 📝 outline | End-to-end feature plus retro |

## Open questions for the author
1. **Tone.** Is the fantasy-tavern flavor right, or should it be more
   neutral/professional (for workplace workshops)?
2. **Length.** Target time per module? (Current guess: 20 to 40 minutes, so 3
   to 4 hours in total.)
3. **Playground language.** Python is the most beginner-friendly. Do we need a
   JS/TS version?
4. **Module 5 depth.** A neutral comparison table, or opinionated
   recommendations? Should players need access to two tools?
5. **MCP build quest.** Required, or a stretch goal? It needs `pip install`.
6. **Deterministic checks.** Add `scripts/check.py` per quest, or rely on
   the GM's judgment?
7. **Workshop mode.** Will this be run live alongside the presentation, or only
   self-paced? This affects pacing and checkpoints.
8. **Non-coders.** Should there be a track for people who don't code at all
   (PMs, analysts)?
