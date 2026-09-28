# Example Scenarios (fallback)

Use one of these when the learner can't think of recent work, or wants to
skip the interview. Build it following the rules in [README.md](README.md),
exactly as for an interview-based project.

## Business: client quarterly report
A consulting team's quarterly engagement report for a client.
- **Inputs:** `data/engagements.csv` (projects, regions, hours, revenue),
  `notes/` (three short meeting notes), `template.md` (report template).
- **Existing output:** `report-q3.md`, which has planted errors: a
  double-counted duplicate row, a mislabelled region, and a summary total that
  doesn't match the data.
- **Slot ideas:**
  - P1.1: the wrong total.
  - P1.2: a regional breakdown (design choice: rank by revenue or by growth).
  - P1.3: a one-page executive summary.
  - P3.1: a "quarterly report" skill.
  - P4.1: a 3-slide deck of the report's key findings.
  - P6.1: the full Q4 report from new data.

## Engineer: utilization tracker
A small command-line tool that logs consultant hours by project and reports
utilization.
- **Code:** `tracker.py` (add, list, and report commands), `hours.json`,
  and `test_tracker.py` (tests that pass at the start).
- **Planted bugs:** overlapping entries are double-counted, and adding hours to
  an unknown project crashes.
- **Slot ideas:**
  - P1.1: the crash.
  - P1.2: a billable vs non-billable split (design choice: flag each entry or
    each project).
  - P1.3: an `export` command that writes a CSV.
  - P3.1: a "release checklist" skill.
  - P4.1: a diagram of how an entry flows through the tracker.
  - P6.1: team-level reporting.
