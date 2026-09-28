# Module 1: Prompting

> *The barkeep points at a notice board covered in bug reports.
> "Words are your sword here. Swing them carelessly and you'll cut the wrong thing."*

## Learning objectives
- Understand why "fix the bug" gets worse results than a specific task prompt.
- Write prompts with the four parts agents need: **Goal, Context, Constraints,
  Done-when**.
- Use **plan-first** prompting: have the agent propose a plan, review it, then
  let it build.
- Ask the agent to **verify its own work** (run tests, reproduce the bug, show
  the output).

## Key ideas

**Chat prompting vs agent prompting.** In chat, you prompt for an *answer*. With
an agent, you prompt for an *outcome*. The agent will take many actions to get
there, so it needs to know when it's done and what it must not touch.

**The GCCD pattern** (a simple checklist, not a magic formula):
| Part | Question it answers | Example |
|------|---------------------|---------|
| **Goal** | What outcome do I want? | "Selling an item that isn't in stock should show a clear error." |
| **Context** | What should it look at? | "The logic is in `playground/tavern.py`, `sell()`." |
| **Constraints** | What must not change? | "Don't change the ledger file format. Standard library only." |
| **Done-when** | How do we know it worked? | "Add a test for it. All tests pass." |

**Plan first, then build.** For anything non-trivial, ask for a plan before any
code. Many tools have a dedicated plan mode for this. It's cheaper to fix a
plan than a pile of wrong changes.

**Verification.** Agents are much more reliable when they can check themselves.
Ask for tests, a reproduction, or command output as proof.

**Adept track note:** stress what's different from ChatGPT habits. There's less
need for long role-play preambles ("You are an expert...") and more need for
concrete file paths, constraints, and success criteria.

## Quests
| # | Quest | Summary |
|---|-------|---------|
| 1 | [Vague vs Specific](quests/01-vague-vs-specific.md) | Try "fix the bug", then rewrite it with GCCD |
| 2 | [Plan Before You Build](quests/02-plan-first.md) | Get a plan, critique it, then run it |
| 3 | [BOSS: Proof of Work](quests/03-boss-proof-of-work.md) | One prompt that ships a feature *and* proves it works |
