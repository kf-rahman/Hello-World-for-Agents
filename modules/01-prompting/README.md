# Module 1: Prompting

**Time:** 25 minutes

## Learning goal
The learner can write a prompt that an agent can carry out **without guessing**:
it states the outcome, where to look, what not to change, and how to confirm the
work is done.

## Objectives
- Explain why "fix the problem" gives worse results than a specific task prompt.
- Write prompts with four parts: **Goal, Context, Constraints, Done when**.
- Use **plan first**: ask for a plan, review it, then approve the work.
- Ask the agent to **verify** its own work.

## Key concepts

**Prompting for an answer vs prompting for an outcome.** In a chat, you prompt
for an answer. With an agent, you prompt for an outcome, and the agent takes
many steps to get there. It needs to know what "done" means and what it must
not touch, because every guess it makes carries into the steps that follow.

**Goal, Context, Constraints, Done when.** A checklist, not a formula:

| Part | The question it answers |
|------|-------------------------|
| **Goal** | What outcome do I want? |
| **Context** | Which files, data, or background should the agent use? |
| **Constraints** | What must stay the same? What's off limits? |
| **Done when** | How will we know it worked? |

**Plan first.** For anything that isn't trivial, ask for a plan before any
changes. Many tools have a plan mode, and in any tool you can say "don't change
anything yet; give me a plan." Fixing a plan is cheaper than undoing work.

**Verification.** Agents are more reliable when they can check themselves. Ask
for proof: tests passing, the output shown, figures reconciled against the
source.

## Persona notes
- **Engineer:** "done when" usually means tests: a new test that covers the
  change, and all tests passing.
- **Business:** "done when" usually means the output can be checked: totals
  match the source, every claim cites where it came from, and the output
  follows the required format.
- **Adept:** point out the chat-era habits that matter less here, such as long
  role-play openings ("You are an expert…"). Concrete file names, constraints,
  and success criteria matter more.

## Exercises
| # | Exercise | Minutes |
|---|----------|---------|
| 1 | [Vague vs Specific](exercises/01-vague-vs-specific.md) | 10 |
| 2 | [Plan First](exercises/02-plan-first.md) | 7 |
| 3 | [Checkpoint: One Prompt, Verified Result](exercises/03-checkpoint.md) | 8 |
