# Modern Software Development with Git, GitHub & CI/CD

A 1.5-day intensive course on professional software development
practices — version control, collaborative workflows, environment
management, CI/CD, testing, and documentation — taught through one
continuous narrative and one shared codebase.

## What this course is (and isn't)

**This is not a tool tutorial.** Git, GitHub, Conda, Docker, pytest,
GitHub Actions — each has its own excellent documentation, and this
course won't try to out-teach it. Reading the manual is your job, both
during the course and long after it.

**This course teaches the *principles* those tools implement**, so that
the next tool you meet — a different CI system, a different package
manager, whatever replaces today's stack in five years — is a small
translation, not a from-scratch relearn:

* **Version control as collaboration**, not just backup — why history,
  branches, and review exist, and what breaks without them
* **Reproducibility** — why "works on my machine" happens, and the
  discipline (pinned environments, containers) that prevents it
* **Automation as a discipline** — why CI/CD replaces manual, human-run
  checklists, and what that actually buys a team under pressure
* **Testing as design feedback**, not a checkbox exercise run once
  before release
* **Documentation as a deliverable**, not an afterthought bolted on at
  the end

Every session picks *one* concrete tool to make a principle tangible —
Git/GitHub for version control, Conda/Docker for reproducibility, pytest
for testing, GitHub Actions for CI/CD. Learn the tool well enough to
practice the principle; go deep on the tool itself with its own docs
afterward, if and when you need to.

## Audience

Basic Python programming knowledge. No prior Git or GitHub experience
assumed. Python-only — there is no C++ track.

## Format

Four sessions across a day and a half (schedule below), building toward
one capstone: a small team project run the way a real project runs —
fork, branch, pull request, review, merge, conflict, retrospective.

| | Time | Session |
|---|---|---|
| **Day 1** | 9:00–9:30 | Icebreaker & course overview |
| | 9:30–10:30 | [Session 1 — Git & GitHub basics](1-software-development-basics/) |
| | 10:45–12:15 | [Session 2 — Environment control](2-environment-control/) |
| | 13:30–14:00 | (S)nap Talk — GitHub Copilot intro |
| | 14:00–15:45 | [Session 3 — Documentation & testing](3-documentation-testing/) |
| | 15:45–16:45 | [Session 4 — Workflow control (CI/CD)](4-workflow-control/) |
| | 16:45–17:45 | [Session 5 (1/3) — Data challenge tag-up](5-data-challenge/) |
| *(evening, optional)* | | Teams implement their claimed backlog task |
| **Day 2** | 9:00–11:15 | [Session 5 (2/3) — Merge & integration](5-data-challenge/) |
| | 11:15–12:15 | [Session 5 (3/3) — Wrap-up & retrospective](5-data-challenge/) |

## What you'll actually do

Every principle above gets practiced on the same running example: a
small [astro-image pipeline](5-data-challenge/) (load → stack → detect
stars → measure their brightness → composite image), built collaboratively
by teams of 2–3 who fork the shared repo, split the work, and integrate
it back — conflicts, review, and all — under the actual time pressure a
real project runs under. Sessions 1–4 are the concepts and a live demo
each; the [data challenge](5-data-challenge/) is where they all get used
at once, for real, against a repo you didn't write.

## Repo layout

* [`1-software-development-basics/`](1-software-development-basics/) — Git & GitHub, the collaborative workflow
* [`2-environment-control/`](2-environment-control/) — Conda/Miniforge & Docker, reproducibility
* [`3-documentation-testing/`](3-documentation-testing/) — docstrings, doctest, PyTest, mocking
* [`4-workflow-control/`](4-workflow-control/) — pixi, GitHub Actions, CI/CD
* [`5-data-challenge/`](5-data-challenge/) — the capstone workshop (schedule, team workflow, backlog)

## License

GPLv3 — see [`LICENSE`](LICENSE).
