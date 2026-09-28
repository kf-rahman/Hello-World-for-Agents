# Presentation Brief

Working notes for the presentation that goes with *Hello World for Agents*.
Use this file to pick up where we left off, in any session or tool.

## Where we left off (2026-09-28)
- The course content for all 7 modules is drafted (see `docs/COURSE_DESIGN.md`).
  The practice projects are still to be decided.
- The key messages below are agreed by the author.
- The measurement framework below is a **proposal**, waiting for the author's
  answers to the open questions.
- A separate session started on the slide outline, working on branch
  `claude/presentation-planning`. It began before this brief existed, so point
  it to this file.
- `docs/PRESENTATION.md` is an older placeholder that still has the discarded
  fantasy framing. This brief replaces it.

## Key messages (from the author)

1. **Leaders and senior staff have to drive this.** The push toward agentic
   workflows has to come from people leaders and senior staff. They show what
   it looks like by working this way themselves, and they encourage their peers
   to work at this pace. Adoption follows what senior people do and make room
   for, not tool licences.

2. **These tools let you choose between depth and speed.** You can now decide
   where to learn something very deeply and where to move very fast.
   - Example: **building a report**. A report has a lot of baggage: data
     extraction, cleaning, analysis, visuals, narrative, and QA. Each part used
     to take roughly fixed effort. Now you choose which parts to spend more
     time on. For example:
     - depending less on a very technical person to extract the data, or
     - exploring visuals to understand what could have the most impact.

3. **Be intentional about every working session.** Set clear success criteria
   before you start. This is the Goal / Context / Constraints / Done when
   pattern from Module 1, so the talk and the course reinforce each other.

4. **Measure success** (see below). Success criteria for each session are the
   small-scale version of measuring success for the whole rollout.

## How the industry measures success (research summary)

**Consulting firms track adoption first.**
- McKinsey reports that about 72% of its roughly 45,000 staff actively use its
  internal tool, Lilli, with about 500,000 queries a month.
- All the large firms have rolled out internal assistants. PwC's is the largest
  by seat count, at about 200,000.

**What they've learned: adoption isn't value.**
- McKinsey found that 88% of organizations use AI, but only about 6% get
  significant profit from it.
- BCG found that only about 1 in 4 executives see significant returns.
- MIT's "GenAI Divide" report (2025) found that 95% of pilots showed no
  measurable profit-and-loss impact.

**Three findings to design the measurement around**

| Finding | What it means for measuring |
|---|---|
| **BCG/Harvard "jagged frontier" study** (758 consultants, 2023). On tasks the AI handles well, consultants completed 12.2% more tasks, 25.1% faster, and at higher quality. On tasks outside what it handles well, they were 19 percentage points *less* likely to reach the correct answer. | Measure quality, not only speed. |
| **METR study** (2025). Experienced developers were 19% *slower* with AI but believed they were 20% faster. METR now describes this result as historical. | Don't rely only on people's own estimates of time saved. |
| **NBER working paper 35275** (2026, "Writing Code vs. Shipping Code"). Coding agents greatly increased the amount of code written, but actual releases rose only about 30%, because human review became the bottleneck. | Measure the finished deliverable, not how much the agent produced. |

Main framework in software engineering: DX's **utilization, impact, cost**.

## Proposed measurement framework (adapted for consulting)

| Layer | Question | Example metrics | Leading or lagging |
|---|---|---|---|
| 1. Learning | Can people do it? | Course completion, capstone passed, confidence before and after | Leading |
| 2. Practice | Are they doing it well? | Weekly active use; % of working sessions that start with written success criteria; memory files and skills shared across the team (reuse is a strong sign of maturity) | Leading |
| 3. Work impact | Is the work changing? | For 2–3 recurring deliverables: time from request to client-ready; hand-offs to technical specialists; rounds of rework; reviewer quality score; **where the saved time went** | Middle |
| 4. Business | Does it matter commercially? | Capacity and utilization, margin on fixed-fee work, client satisfaction | Lagging |

"Where the saved time went" ties the measurement to message 2. The claim isn't
only that time is saved; it's that time is spent deliberately. Did it go into
deeper analysis, better visuals, or just more volume?

**How to run it:** a 4–6 week pilot cohort alongside a comparison team.
1. Measure a baseline for 2–3 recurring deliverables before the pilot starts.
2. Collect timestamps for Layer 3, not just surveys.
3. Add a 2-minute weekly check-in for Layer 2.

## Open questions for the author
1. Who is the measurement for: leadership wanting ROI, or teams improving how
   they work? The answer decides whether Layer 4 or Layer 3 leads the talk.
2. Can we get usage data from the tools (seat and usage dashboards), or will this
   rely on surveys and timestamps?
3. Is there a real recurring deliverable to use as the report example? It could
   also become the business persona's practice project.
4. Still to confirm: audience, length, format (Google Slides / PowerPoint /
   other), live demo or not, and whether the talk goes alongside a live run of
   the course.

## Sources
- HBS AI Institute: Navigating the Jagged Technological Frontier:
  https://aiinstitute.hbs.edu/navigating-the-jagged-technological-frontier/
- Harvard Crimson on the BCG study:
  https://www.thecrimson.com/article/2023/10/13/jagged-edge-ai-bcg/
- METR, early-2025 developer productivity study:
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- NBER w35275, Writing Code vs. Shipping Code: https://www.nber.org/papers/w35275
  (Not read directly; secondary sources give different percentages but agree
  releases rose about 30%. Check the paper before quoting exact figures.)
- DX AI measurement framework: https://getdx.com/blog/ai-roi-calculator/
- BCG, AI adoption in 2024:
  https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- BCG, Closing the AI impact gap:
  https://www.bcg.com/publications/2025/closing-the-ai-impact-gap
- AI in consulting, 2026 (McKinsey Lilli figures):
  https://whitehat-seo.co.uk/blog/ai-impact-on-consulting
- Big consulting firms' internal AI tools compared:
  https://consulting-huber.com/ai-consulting-frameworks-compared.html
- MIT GenAI Divide coverage:
  https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx
