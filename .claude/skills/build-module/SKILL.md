---
name: build-module
description: Draft or revise one course module README (1-software-development-basics, 2-environment-control, 3-documentation-testing, 4-workflow-control, or 5-data-challenge) for the Git/GitHub/CI-CD course. Use whenever the user asks to work on "the next module", "module N", or a session README, or references the course TODO list.
---

# Build a course module

This repo teaches Git/GitHub/CI-CD across five sessions, each with its own
module directory (`N-topic/README.md`). Read `CLAUDE.md` at the repo root
first — it has the full course design, the schedule, the team structure,
the source-material → tooling mapping table, and the module README
convention (intro → demo → exercises). Everything below assumes that
context.

## Process for one module

1. **Confirm scope.** Identify which module is next per the root README's
   TODO list (or ask if ambiguous). Only work on one module at a time —
   don't pre-draft later modules.

2. **Read the source material.** Look up the module's row in CLAUDE.md's
   mapping table for which `inputs/<x>/README.md` (and exercise files) to
   base it on. Read those files under `inputs/` — treat them as read-only
   reference, never edit them. Note what needs translating (GitLab → GitHub
   terms, Apptainer → Docker, etc. per the table) and what can be reused
   close to verbatim.

3. **Draft the module README** at `N-topic/README.md` with three parts,
   per CLAUDE.md's "Module README conventions":
   - Short, terse intro (slide-deck style, not prose essay).
   - One runnable demo against the data-challenge repo (or a minimal
     standalone snippet if the data-challenge repo isn't relevant yet,
     e.g. module 1 before it exists).
   - Exercises written as GitHub-Issue-shaped tasks for a 2-3 person team,
     independent of each other, sized to realistically fit a couple hours
     of optional Day 1 evening work (see "Evening work & the Day 2
     workshop" in CLAUDE.md — Day 2 morning is a merge/integration
     session, not more implementation time, so don't over-scope). Each
     task should also have enough internal structure to reward splitting
     it across the team rather than one person doing it solo — the point
     is both inter-team parallelism *and* intra-team collaboration (see
     the backlog-sizing note in CLAUDE.md).
   - **Exception: module 1** doesn't need this exercises part — there's no
     time in Session 1 for a hands-on role-play, so intro + demo only is
     fine (see "Exception: module 1" under CLAUDE.md's "Module README
     conventions"). Its concepts get practiced implicitly through every
     other module's exercises, and developer/reviewer/maintainer roles
     (mapped to real GitHub permission levels: Write/Triage/Maintain) get
     discussed and fixed at the Day 1 tag-up (Session 5 1/3), then applied during
     the Day 2 merge session — not role-played in module 1.

4. **Flag adaptation decisions and open questions inline** as you draft
   (e.g. "old material used X, this uses Y because Z") rather than silently
   picking one — the user reviews every module before it's final.

5. **Stop for review.** Do not move to the next module or auto-commit.
   Present the draft, iterate on feedback, and only commit (one module per
   commit, per CLAUDE.md's commit style) once the user validates it.

## Things to watch for

- The old `inputs/` material is GitLab/Apptainer/Conda-era and CPPM/IN2P3
  specific (SSO, `gitlab.in2p3.fr`, "reporter" role, etc.) — don't port
  those specifics.
- Some old exercise files are empty stubs (e.g. `inputs/conda/ex2-4.md`) —
  don't treat their existence as "content already written."
- Python-only course: skip any C++/CMake/Google Test material even where
  the old `inputs/testing` covers both.
- If a demo or exercise needs something from the data-challenge repo that
  doesn't exist yet, say so explicitly rather than inventing repo state —
  check with the `data-challenge-setup` skill/work first.
