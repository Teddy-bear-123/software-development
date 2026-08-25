---
name: data-challenge-setup
description: Scaffold or update the shared data-challenge codebase that students fork/branch/PR against during Session 5 (a separate GitHub repo, seeded from 5-data-challenge/ in this repo). Use when the user asks to set up, seed, or update the data challenge repository, its starting codebase, or its issue backlog.
---

# Set up the data-challenge repo

Read `CLAUDE.md` at the repo root first, especially the "Repo layout"
(data-challenge repo is separate from this one), "Team structure", and the
`5-data-challenge` row of the mapping table.

The data challenge is a **real, separate GitHub repo** — students need
actual Issues/PRs/Actions/Pages/GHCR against it, which a subfolder of this
repo can't provide. Creating or pushing to a real external GitHub repo is
a visible, hard-to-fully-reverse action (issues, PRs, and branch history
other people will see) — confirm the repo name/org and scope with the user
before creating it or pushing, even if a template already exists locally.

## Process

1. **Resolve the open question first.** CLAUDE.md flags that no exact
   "2023 edition" data-challenge repo was found under `inputs/`; the
   closest precedents are `inputs/eurolabs-os-school/hands-on-2024/` (a
   worked, 39-commit history — the best template for how the capstone
   *plays out*: numbered-issue branches, incremental CI setup, PRs into
   main) and `hands-on-2026/` (a fresh starting-point template). Both are
   C++/ROOT physics-analysis codebases (`project-zero`); this course is
   Python-only. Confirm with the user what the actual challenge domain and
   starting dataset should be before building anything — don't assume
   `project-zero`'s domain carries over, only its *structure* (bare
   "day zero" starting point, no CI/tests/docs yet — those are what
   students add during the workshop).

2. **Design the seed codebase.** A small, working Python codebase with a
   "foundation layer" (shared code all teams build on) deliberately missing
   the things modules 2-4 teach: no env spec, no CI workflow, no docs, no
   tests, no Docker image. That gap is what the Session 5 issue backlog
   fills in. Keep it minimal — this is a teaching prop, not a real project.

3. **Draft the seed content** under `5-data-challenge/` in *this* repo
   first (template/starting-point files + a README describing the
   challenge), so it goes through the normal review-and-commit process
   like any other module.

4. **Only after that's validated**, help stand up the real GitHub repo
   (confirm org/name, visibility, and whether it's created fresh or as a
   "Use this template" repo) and push the seed content as its initial
   commit(s) / `main` branch.

5. **Draft the shared issue backlog** as a set of independent, parallel
   GitHub Issues spanning modules 2-4 plus data-challenge feature work
   (see CLAUDE.md's "Team structure" section for the task shape). Each
   team **forks** the upstream repo to work; internal-to-team process is
   the team's choice, but every team integrates back via a PR from its
   fork. Size each task to realistically fit a couple hours of the
   optional Day 1 evening slot, but with enough internal structure to
   reward splitting it across the team rather than one person doing it
   solo — the backlog should exercise intra-team collaboration, not just
   inter-team parallelism. Tasks get claimed and roles/workflow get fixed
   at the Day 1 tag-up (Session 5 1/3), then Day 2's 9:00-11:15 session is
   dedicated to running the merge with those already-nominated
   maintainers/reviewers, finished teams first, with finished teams then
   supporting teams still working rather than idling (see "Evening work &
   the Day 2 workshop" in CLAUDE.md), so an over-scoped backlog directly
   eats into that integration time. Design the backlog so that different
   teams' PRs are likely to collide on a few shared files (e.g. a shared
   README, CI config, or module) — that's the deliberate merge-conflict
   teaching moment, not something to engineer away.

## Things to watch for

- Don't silently pick the challenge domain/dataset — that's a decision for
  the user, flagged as open in CLAUDE.md.
- Keep parity with module content: if module 3 lands on a specific CI
  workflow shape or module 4 lands on a specific docs tool, the seed repo
  and backlog issues should match what was actually taught, not something
  built ahead of that decision.
- Any action that touches the real external GitHub repo (creating it,
  pushing, opening issues) needs explicit confirmation — don't do it as a
  side effect of an otherwise-local editing task.
- Teams not finishing by the end of Session 5 (2/3) is an expected,
  designed-for outcome (see "Evening work & the Day 2 workshop" in
  CLAUDE.md) — the wrap-up's structured retrospective handles it, don't
  try to prevent it by over-simplifying every task.
