# Playtest Log

## Playtest 1: 2026-09-28
**Setup:** a fresh Claude Code instance (command line, run headless) on a clean
clone of the repo, with no context beyond the repo itself. The tester played
**"Sam"**: novice experience, business persona, "using the desktop app". Actions
were pre-approved, so it behaved like a tool in **auto-approve mode**.
**Scope:** Modules 0 and 1 (6 exercises).

### Results

| Exercise | Result | Notes |
|---|---|---|
| 0.1 Setup | ✅ Pass | Asked one question at a time; created and filled in the save file |
| 0.2 Build Your Project | ✅ Pass | Sam described a client pipeline review deck (CRM export + finance tracker). The guide proposed a scenario that matched Sam's pain points (duplicates, wrong-region deals, reconciliation). Build took **~3 min**. The data independently reconciles to finance once cleaned. An answer-key entry exists for every slot. |
| 0.2 Confidentiality | ✅ Pass | Sam named the client on purpose. The guide flagged it, switched to "Client A, a regional bank", and the name appears in no file. |
| 0.3 Permissions | ⚠️ → ✅ Fixed | **Bug:** in auto-approve mode the guide carried out the delete it had just told Sam to deny (it recovered from the backup). **Fix:** it now asks whether a prompt appeared and, if not, doesn't attempt the delete. Retested: works. |
| 1.1 Vague vs Specific | ✅ Pass | The vague prompt led to a "force the total to match" proposal with its assumptions listed. Sam's structured prompt found 2 duplicates and 1 wrong region; constraints were respected (checked in the files). |
| 1.2 Plan First | ✅ Pass | The plan surfaced a real design choice. Sam changed it; the guide followed the revised plan and suggested an out-of-scope follow-up rather than just doing it. |
| 1.3 Checkpoint | ✅ Pass | One prompt produced a data-quality note with checks passing. The guide listed 6 assumptions and gave useful feedback on the prompt. |

### Other observations
- **Resuming works.** A brand-new session picked up the learner's position
  from `save/save.md` alone.
- **Pacing.** The agent's own processing time for Modules 0–1 was about 10
  minutes, leaving plenty of the 35-minute budget for the learner's reading and
  writing.
- **Cost.** About **$2.80** of model usage for Modules 0–1 on a top-tier model.
- **The guide runs `check` on its own** once a task is done, rather than
  waiting for the learner to type it. That feels smooth; left as is.
- **Tool-specific settings.** When asked where plan mode or permission settings
  are in the desktop app, the guide admitted it wasn't sure and pointed to the
  official docs, as instructed.

### Not covered yet
- Modules 2–6.
- The engineer persona.
- Real permission prompts (this run auto-approved everything).
- Tools other than Claude Code (for example Copilot or Codex).
- What the learner sees while the project is being built (headless runs only
  show each turn's final reply).
