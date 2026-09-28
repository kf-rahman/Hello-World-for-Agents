# Module 3: Tools & Skills

> *The blacksmith's wall is covered in tools. "A good smith knows every tool.
> A great one makes their own."*

## Learning objectives
- Understand a **tool call**: the model asks, the harness runs it, and the
  result comes back into context.
- Know the built-in tool families: read/search, edit, shell, web, and sub-agents.
- Set **permissions** on purpose: allowlists, deny rules, and modes.
- Write a **skill**: a reusable, packaged set of instructions (and optionally
  scripts) the agent loads when it's relevant.
- Know the related concepts: **custom commands**, **hooks**, and **sub-agents**,
  and when each fits.

## Key ideas (draft)
- A tool is just a function with a description. The model reads the
  description to decide when to use it, so **descriptions are prompts**.
- **Skills vs memory:** memory is always loaded; a skill loads only when it's
  relevant. Skills keep context lean.
- **Skills are becoming portable.** The `SKILL.md` format started in Claude
  Code and is now supported in other tools. *(GM/maintainers: check current
  support per tool before teaching.)*
- **Hooks** are for rules that must *always* happen (for example, run the
  formatter after every edit). Don't rely on the model to remember them.

## Planned quests
| # | Quest | Summary |
|---|-------|---------|
| 1 | X-Ray Vision | Ask the agent to list its own tools and explain what one tool call looked like |
| 2 | Allowlist | Allow running the tests without a prompt, but keep deletes gated |
| 3 | Forge a Skill | Write a `tavern-release` skill: run tests, bump version, write a changelog entry |
| 4 | BOSS: Skill Check | A fresh session gets asked to "cut a release" and uses the skill without being told to |

**Note:** the skill lives in the tool's skill folder (for example
`.claude/skills/tavern-release/SKILL.md`), so the GM must allow that path.
