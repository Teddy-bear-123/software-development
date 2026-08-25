---
name: data-challenge-setup
description: Scaffold or update the shared data-challenge codebase that students fork/branch/PR against during Session 5 (a separate GitHub repo, cloned locally at data-challenge/). Use when the user asks to set up, seed, or update the data challenge repository, its starting codebase, or its issue backlog.
---

# Set up the data-challenge repo

Read `CLAUDE.md` at the repo root first, especially "Repo layout", "Team
structure", "Evening work & the Day 2 workshop", and the `5-data-challenge`
row of the mapping table (domain decision + rationale).

The data challenge is a **real, separate GitHub repo**
(`git@github.com:jzoubian/software-development_data-challenge.git`), already
created and cloned locally at `data-challenge/` (gitignored in this repo,
same treatment as `inputs/` — never commit its files into *this* repo's
history; commits/pushes happen from inside `data-challenge/` against its
own remote). Pushing to it is a visible, hard-to-fully-reverse action —
confirm with the user before pushing, even though the repo/clone already
exist.

`5-data-challenge/` (in *this* repo) is teaching content only — intro
slides, schedule, backlog/exercise descriptions for students. It is not
where the codebase lives and is not seeded from the codebase or vice versa;
keep them in sync by hand when either changes.

## Decided domain (don't re-litigate without asking)

A tiny **astro-image pipeline**: load frames → stack/denoise → detect
sources → basic aperture photometry → false-color composite. Synthetic,
seeded star-field data (Gaussian point sources + Poisson noise) for
dev/tests — fully reproducible, no download dependency. The "real image"
payoff is a **bonus, stubbed** `astrolab.realdata.fetch_sky_image` that
queries a public sky-survey archive live via `astroquery` (SkyView/DSS —
confirmed working: `SkyView.get_images(position="M42", survey=["DSS"],
pixels=200)`), not a bundled downloaded file — sidesteps licensing
entirely and doubles as a live example of the reproducibility-vs-network
tradeoff for modules 2/3. Python-only, numpy/matplotlib core +
astropy/astroquery for the bonus module — beginner-friendly, no astronomy
background assumed of students.

## Process

1. **Design the seed codebase.** A small, working foundation layer
   (shared code all teams build on) deliberately missing what modules 2-4
   teach: no env spec, no CI workflow, no docs, no tests, no Docker image.
   That gap is what the Session 5 issue backlog fills in. Concretely:
   an image loader/`AstroImage`-style wrapper, and a thin `pipeline.py`
   that orchestrates calls into feature functions that don't exist yet —
   that file is the deliberate shared collision point for the Day 2
   merge. Keep it minimal — this is a teaching prop, not a real project.

2. **Draft directly in `data-challenge/`**, since it's already the real
   repo — synthetic data generator, foundation-layer code, and a
   student-facing README describing the challenge and how to get started.
   Go through the normal review-and-commit process before pushing to the
   remote.

3. **Verify it actually runs** (fresh env, run the pipeline end to end)
   before presenting it as done — a seed repo that doesn't run out of the
   box undermines the whole workshop.

4. **Only after that's validated with the user**, push to `origin`
   (confirm branch/force-push status, don't push over unreviewed content).

5. **Draft the shared issue backlog** as a set of independent, parallel
   GitHub Issues spanning modules 2-4 plus data-challenge feature work
   (see CLAUDE.md's "Team structure" section for the task shape, and the
   backlog sketch in the domain decision above: env spec, CI workflow,
   Dockerfile+GHCR, docstrings+doctest+Pages, PyTest coverage, stacking,
   source detection, photometry, false-color composite, contrast
   stretch, and the bonus `fetch_sky_image` real-image feature). Each
   team **forks** the upstream repo to work;
   internal-to-team process is the team's choice, but every team
   integrates back via a PR from its fork. Size each task to realistically
   fit a couple hours of the optional Day 1 evening slot, but with enough
   internal structure to reward splitting it across the team rather than
   one person doing it solo — the backlog should exercise intra-team
   collaboration, not just inter-team parallelism. Tasks get claimed and
   roles/workflow get fixed at the Day 1 tag-up (Session 5 1/3), then Day
   2's 9:00-11:15 session is dedicated to running the merge with those
   already-nominated maintainers/reviewers, finished teams first, with
   finished teams then supporting teams still working rather than idling
   (see "Evening work & the Day 2 workshop" in CLAUDE.md), so an
   over-scoped backlog directly eats into that integration time. Design
   the backlog so that different teams' PRs are likely to collide on a
   few shared files (e.g. `pipeline.py`, `README.md`, CI config) — that's
   the deliberate merge-conflict teaching moment, not something to
   engineer away.

## Things to watch for

- Keep parity with module content: if module 3 lands on a specific CI
  workflow shape or module 4 lands on a specific docs tool, the seed repo
  and backlog issues should match what was actually taught, not something
  built ahead of that decision.
- Any action that touches the real external GitHub repo (pushing, opening
  issues on GitHub itself, changing repo settings) needs explicit
  confirmation — don't do it as a side effect of an otherwise-local
  editing task.
- Teams not finishing by the end of Session 5 (2/3) is an expected,
  designed-for outcome (see "Evening work & the Day 2 workshop" in
  CLAUDE.md) — the wrap-up's structured retrospective handles it, don't
  try to prevent it by over-simplifying every task.
