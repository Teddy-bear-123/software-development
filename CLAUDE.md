# Modern Software Development with Git, GitHub & CI/CD — course repo

This repo holds the instructor materials for a 1.5-day intensive course teaching
professional software development practices — version control, collaborative
workflows, environment/dependency management, CI/CD, testing, and
documentation — through one continuous narrative and one shared codebase.

Audience: students with basic Python programming knowledge, no prior Git/GitHub
experience assumed. Format: Python-only (no C++ track).

## Repo layout

- `README.md` — course overview, goals, schedule, resources (student-facing).
- `1-software-development-basics/` — Session 1: Git & GitHub collaborative workflow.
- `2-environment-control/` — Session 2: dependency & environment management.
- `3-workflow-control/` — Session 3: reproducible workflows & CI/CD basics.
- `4-documentation-testing/` — Session 4: docstrings/Markdown docs + PyTest.
- `5-data-challenge/` — Session 5: the data challenge workshop (capstone).
- `inputs/` — **read-only reference material** from past editions of related
  trainings (separate nested git repos, gitignored, never committed here).
  Each module is *adapted from* one or more of these, not copied verbatim —
  see the mapping table below. Do not edit files under `inputs/`.

The data challenge itself (the shared codebase students fork/branch/PR
against) lives in **a separate GitHub repo**, not in this repo — students
need real Issues/PRs/Actions/Pages/GHCR, which only works against an actual
GitHub repo. This repo keeps a seed/template copy of its starting content
under `5-data-challenge/` and documents how to stand the real repo up from it.

## Working process

Course content is built one TODO item at a time, top to bottom. For each
item: draft it, review with the user, iterate, and get it **committed**
before starting the next item. Don't pre-draft multiple modules ahead of
where the user currently is — later modules may change based on decisions
made while building earlier ones (timing, tone, depth). Use the
`build-module` skill for drafting/revising a module README; use the
`data-challenge-setup` skill for the shared challenge repo.

Commit style: atomic, one module/deliverable per commit, matching the
TODO breakdown in the course proposal.

## Format & schedule (validated)

Four sessions across 1.5 days (3h + 3h + 4h):

**Day 1**
- 9:00–9:30 Icebreaker & course overview
- 9:30–10:30 Session 1 — Git & GitHub collaborative workflow
- 10:45–12:15 Session 2 — Environment control
- 13:30–14:00 (S)nap Talk — GitHub Copilot intro
- 14:00–15:00 Session 3 — Workflow control
- 15:00–15:30 Session 4 (1/2) — Documentation (Markdown & docstrings)
- 15:45–16:45 Session 4 (2/2) — Testing (PyTest)
- 16:45–17:45 Session 5 (1/3) — Data challenge intro, team formation,
  tag-up: assign backlog tasks **and discuss and fix roles
  (maintainer/reviewer) and workflow conventions** for the merge session,
  before evening work starts

**Day 2**
- 9:00–11:15 Session 5 (2/3) — Data challenge workshop: apply the roles
  and workflow fixed the day before to actually merge (integration-focused,
  see below — not more implementation time; finished-first ordering, then
  peer support for teams still working, see below)
- 11:15–12:15 Session 5 (3/3) — Data challenge wrap-up: merge whatever's
  ready, then a **structured retrospective** (not just a buffer) — see
  below

## Evening work & the Day 2 workshop

Sessions 2–4 are lecture + live demo only, with no dedicated per-module
exercise slot — all hands-on implementation for modules 2–4 (environment,
workflow/CI, docs, testing) plus the data-challenge feature work happens
against the backlog assigned at the end of Session 5 (1/3):

- **Day 1, Session 5 (1/3), 16:45–17:45 — tag-up**: assign backlog tasks,
  and, critically, **discuss and fix the roles and workflow conventions
  here** (who is maintainer/reviewer, branching/PR conventions, how
  conflicts will get resolved) — this is decided as a group before anyone
  starts implementing, not improvised on Day 2.
- **Optional, non-mandatory evening work** (Day 1 evening, unscheduled):
  each team **forks** the shared upstream repo and implements its claimed
  task(s) inside that fork. How the team organizes internally (their own
  branches, who does what, whether they PR to each other) is entirely
  their choice — but integrating back to the shared upstream always
  happens via a **PR from the team's fork**, following the workflow fixed
  at tag-up, aiming to have that PR ready before Day 2 morning.
- **Day 2, Session 5 (2/3), 9:00–11:15 is a merge/integration session, not
  more implementation time**: maintainers/reviewers (already nominated at
  tag-up) run the merge. **Merge order: teams that are done go first.**
  Once a team's PR is merged, that team doesn't sit idle — they move to
  helping teams still working (debugging, pairing, unblocking), so
  finished teams actively reduce the number of teams still stuck rather
  than just watching. Discuss and resolve conflicts live where independent
  PRs touch the same files as they come up.
- **11:15–12:15, Session 5 (3/3) — wrap-up**: merge whatever else is
  ready. **If some teams still haven't finished, that's fine — stop
  there.** Don't extend the coding time; instead run a structured
  retrospective on *why*, framed as "how would this play out on a real
  project": what was the bottleneck, was the task/spec ambiguous or
  under-specified, was the timeline realistic, was the work split
  reasonably within the team, how would you use a backlog/re-scope/
  reassign in this situation. This retrospective is as much the point of
  Session 5 as the merge itself.

⚠️ **Backlog-sizing risk, mitigated by design, not avoided**: not every
team will finish the evening work, and that's treated as expected rather
than a failure to prevent — the finished-first merge order + peer support
+ retrospective (above) are the actual mitigation, not "hope everyone
finishes." What *does* need active design care: each backlog task must be
small enough for a team of 2-3 to complete in a couple hours of evening
work, but **complex enough that the team benefits from splitting the work
internally** — the point isn't just inter-team parallelism (independent
tasks across teams), it's also giving each team a taste of intra-team
collaborative workflow. Tune task granularity for this balance when
drafting the backlog, not just for total time budget.

Cross-reference: there's no time in Session 1 (60 min) for a hands-on
role-play exercise like `inputs/gitlab`'s maintainer/developer/reporter
setup — module 1 teaches commit/branch/issue/PR/review as concepts +
live demo only. The maintainer/reviewer roles and the team's actual
workflow get **discussed and fixed at the Day 1 tag-up (Session 5 1/3)**,
then **applied** during the Day 2 merge session — not role-played inside
module 1 itself. Module 1 should still explain what those roles mean so
tag-up isn't introducing new vocabulary under time pressure; it just
doesn't run the role-play itself — the data challenge (tag-up decides
roles/workflow, evening implementation, Day 2 merge) is the role-play.

## Team structure (data challenge workshop)

Many small teams of 2–3 students (not two fixed teams). Each team **forks**
the shared upstream data-challenge repo — internal-to-team workflow
(branches, who does what, whether they PR to each other inside the fork)
is entirely the team's own choice, but integrating back always happens via
a **PR from the team's fork to the shared upstream**, which is the actual
integration point at Day 2's merge session. There is one shared backlog of
independent, parallelizable tasks (GitHub Issues) spanning all of modules
2–4 plus data-challenge feature work — e.g. "add a pixi/conda-forge env
spec", "add a GitHub Actions test workflow", "write docstrings + doctest
for module X", "add PyTest coverage for module Y", "add a Docker image +
GHCR push", "implement data-challenge feature Z". Teams claim tasks at the
Day 1 tag-up (Session 5 1/3), where roles (maintainer/reviewer) and
workflow conventions also get discussed and fixed for the group — then
fork, implement, and open a PR on their own during the optional Day 1
evening slot (see "Evening work & the Day 2 workshop" above), following
that agreed workflow. The Day 2 morning session is integration, not more
implementation: the maintainers/reviewers nominated at tag-up run the
merge, finished teams first, with finished teams then supporting teams
still working rather than sitting idle (see "Evening work & the Day 2
workshop" for the full merge-order and retrospective flow). The backlog
should be scoped so that independent-task PRs from different teams are
likely to touch overlapping files (e.g. a shared `README.md`, a shared CI
config, a shared module) and produce genuine merge conflicts to resolve
during integration — that collision is a deliberate teaching moment, not
an accident to avoid. Each task should also be sized to reward splitting
the work *within* the team, not just sized for total time — see the
backlog-sizing note above.

## Module content: source material → target tooling

Every item in `inputs/` is GitLab/Apptainer/Conda-era material and needs
adapting, not copying. Old content is CPPM/IN2P3 training material
(`gitlab.in2p3.fr`); terminology, SSO, and CI examples are GitLab-specific
throughout and must be translated.

| Module | Source(s) in `inputs/` | Adapt from → to |
|---|---|---|
| `1-software-development-basics` | `gitlab/` | GitLab (Issues/MRs/"reporter" role/GitLab flow) → GitHub (Issues/PRs/reviewers/GitHub flow). GitHub flow is simpler than GitLab flow — reframe the branching-strategy comparison slide rather than porting it 1:1. |
| `2-environment-control` | `conda/`, `apptainer/` | Conda/Miniforge material ports mostly as-is (already recommends Miniforge over Anaconda). Apptainer → Docker for the CI/CD half; keep Miniforge (not Apptainer) for the local dev-env half. Keep the reproducibility-vs-replicability framing (Konrad Hinsen) and the closing comparison table; keep brief Guix/Nix mention as the "bitwise exact" extreme, but the focus is industry-standard tooling (Conda/Miniforge, Docker), not Guix/Nix. `conda/ex2-4.md` are empty stubs from the original — only `ex1` has real content; the new exercises for this module live in the Session 5 backlog per the schedule note above, not as standalone ex-files. |
| `3-workflow-control` | `workflow/` (thin — mostly notebook-workflow best practices, not pipelines), `eurolabs-os-school/03_snakemake_intro.pdf` (Snakemake, not yet unpacked into hands-on material) | Reframe around **GitHub Actions** CI/CD + **pixi** for the dev environment (pixi isn't industry-standard yet, but worth surfacing as good practice). Mention scripts-with-version-control, Snakemake, DVC only briefly as the broader landscape — don't build deep hands-on content for them. Reuse: the devcontainer+miniforge pattern already in `workflow/.devcontainer/devcontainer.json`, and the notebook version-control best practices (clear outputs before commit, etc.) if notebooks come up at all. GitHub Actions content itself has no precedent in `inputs/` — build fresh. |
| `4-documentation-testing` | `doc/`, `testing/` (Python-only parts: `part-2-simple-ut-particle/python/`, `part-3-cache-mock/python/`) | Docs half ports mostly as-is: docstrings → doctest → API docs (Sphinx/pdoc/mkdocstrings), README essentials. Testing half: reuse the Particle/physics unit-test exercise and the Cache/mock exercise (manual mock + `unittest.mock`); **drop** `part-1-malt-bug` (C/autotools-specific bug hunt) and all C++ mirrors — Python-only per course decision. |
| `5-data-challenge` | `eurolabs-os-school/hands-on-2024/` (worked, 39-commit history — best template for how the capstone *plays out*: numbered-issue branches, incremental CI setup, MRs into main), `eurolabs-os-school/hands-on-2026/` (fresh starting-point template) | No exact "2023 edition" data-challenge repo was found under `inputs/`; the closest precedents are the 2024/2026 `project-zero` hands-on repos (C++/ROOT physics analysis). **Open question for the user**: confirm whether a 2023-edition data-challenge repo exists elsewhere (not under `inputs/`), or whether `hands-on-2024`/`hands-on-2026` are in fact what was meant — and decide the data challenge's own domain/dataset, since `project-zero` is C++/ROOT-specific and this course is Python-only. |

## Module README conventions

Each module README (`N-topic/README.md`) has three parts, in order:

1. **Short intro** — concepts only, slide-deck style (terse headers/bullets,
   not prose essay), enough to run the live demo and understand *why*.
2. **Demo** — one runnable example students execute on their own laptop,
   against the data-challenge repo (or a minimal standalone snippet for
   Session 1 before the data-challenge repo exists yet). Instructor runs it
   live immediately after the intro; students follow along.
3. **Exercises** — tasks for the shared backlog assigned at the end of
   Session 5 (1/3) and implemented mainly during the optional Day 1
   evening slot (see "Evening work & the Day 2 workshop" above), scoped
   for a team of 2–3, independent of the other exercises in the same list
   so teams can pick any subset in parallel. Each exercise should read
   like a GitHub Issue the team would actually open/claim, not a numbered
   homework problem — sized to realistically fit a couple hours of evening
   work, but with enough internal structure that the team benefits from
   splitting it into sub-tasks rather than one person doing it solo (see
   the backlog-sizing note under "Evening work & the Day 2 workshop").

**Exception: module 1.** Session 1 has no time for a hands-on role-play
exercise (see "Cross-reference" above), so `1-software-development-basics`
doesn't need its own backlog-style exercises the way modules 2-4 do — its
mechanics (commit, branch, issue, PR, review) get practiced implicitly
through every other module's exercises, and the maintainer/reviewer roles
specifically get discussed and fixed at the Day 1 tag-up (Session 5 1/3)
and then applied during the Day 2 merge session. Intro + demo only for
module 1 is fine.

## Tooling decisions already made

- Git hosting/collaboration: **GitHub** (Issues, PRs, Actions, Pages, GHCR) —
  not GitLab.
- Local dev environments: **Miniforge/conda-forge**, with **pixi**
  introduced in module 3 as forward-looking practice.
- Containers: **Docker**, pushed to **GitHub Container Registry** via
  GitHub Actions — not Apptainer/Kaniko (those were HPC-specific choices
  in the old material and don't fit a GitHub-based course).
- Docs: docstrings + doctest, published as a site via **GitHub Pages**
  (Sphinx/mkdocstrings/pdoc — pick one when drafting module 4).
- Testing: **PyTest**, `unittest.mock` for mocking.
- AI pair-programming: **GitHub Copilot**, introduced day 1 after the
  team-formation break, before hands-on work begins.

## Note on this repo's own tooling vs. what it teaches

Per the user's global preferences, *this repo's own* scripts/tooling (if
any — e.g. building slides, linting the READMEs) should use `nix-shell`
(or `uv` for Python), matching `inputs/gitlab`'s existing `shell.nix`
pattern. That is separate from what the *course content itself* teaches
students to use (Miniforge/pixi/Docker) — don't conflate the two.
