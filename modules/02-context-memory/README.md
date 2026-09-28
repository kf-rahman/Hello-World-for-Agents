# Module 2: Context & Memory

**Time:** 20 minutes

## Learning goal
The learner can control **what the agent knows**: they give it lasting project
knowledge through a memory file, and they recognize when to start a fresh
session with a handoff note instead of continuing a long one.

## Objectives
- Explain the **context window**: the agent's working memory, which has a limit.
- Name what fills it (messages, files read, tool output) and what happens when
  it's full (older content is summarized or dropped).
- Write a project **memory file** that improves every future session.
- Hand off a task to a fresh session using a short notes file.

## Key concepts

**Agents start each session with no memory.** A new session doesn't remember
earlier ones. Anything the agent should always know has to be written down
where it will be loaded.

**Memory files.** Plain text files that the agent loads automatically at the
start of every session. The idea is the same across tools, but the file names
differ:

| Tool | Project memory file |
|------|---------------------|
| Codex, Cursor, Copilot, and many others | `AGENTS.md` |
| Claude Code | `CLAUDE.md` (can import `AGENTS.md`) |
| Gemini CLI | `GEMINI.md` (configurable) |

*(Check the current conventions in each tool's docs; they change.)* This
course runs on this mechanism: `AGENTS.md` is what makes the agent behave as
your guide, and `save/save.md` is how it remembers your progress.

**What belongs in a memory file:** how to run and check the project,
conventions, known problems, and preferences. **What doesn't:** anything the
agent can easily find out by reading the files itself.

**Context gets noisy.** Long sessions full of dead ends, large outputs, and
off-topic tangents make answers worse. Tools summarize (compact) old context
automatically, and that loses detail. It's often better to start a new session
with a clear handoff note.

## Persona notes
- **Engineer:** memory files hold build and test commands, code style, and
  architecture notes.
- **Business:** memory files hold house style, the audience, definitions
  (for example, what "active customer" means), and the sources to trust.

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [No Memory Between Sessions](exercises/01-no-memory.md) | 4 |
| 2 | [Write a Memory File](exercises/02-memory-file.md) | 8 |
| 3 | [Checkpoint: The Handoff](exercises/03-checkpoint-handoff.md) | 8 |
