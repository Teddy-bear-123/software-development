# 5. Data Challenge — Team Workshop

Session 5 · 3 parts, ~4h15 total, spanning both days · the capstone —
everything from Sessions 1–4 gets *applied*, not lectured, here

| Part | When | What |
|---|---|---|
| 5 (1/3) — Tag-up | Day 1, 16:45–17:45 | Team formation, backlog walkthrough, fix roles & workflow |
| 5 (2/3) — Merge session | Day 2, 9:00–11:15 | Integrate PRs into upstream, finished-first |
| 5 (3/3) — Wrap-up | Day 2, 11:15–12:15 | Merge what's left, structured retrospective |

## Prerequisites

* Everything from Sessions 1–4: Git/GitHub basics, a local clone of the
  data-challenge repo, Conda/Docker installed, `pytest`/`pdoc` installed
* `gh` CLI strongly recommended for today (`gh auth login` if not already);
  the web UI works too, commands below show both
* Read `data-challenge/README.md` if you haven't — the mission, the
  pipeline stages, and why the repo currently stops at `NotImplementedError`

## Objectives

* Turn Sessions 1–4's concepts into one real fork → branch → PR → review →
  merge cycle, against a repo you didn't write
* Practice the developer/reviewer/maintainer roles from Session 1 for real,
  not as vocabulary
* Experience — and resolve — a genuine merge conflict, because the backlog
  is built to produce one
* Run a retrospective that treats "we didn't finish" as data, not failure

## The mission, recap

```
load frames → stack/denoise → detect sources → measure photometry → composite
```

Five noisy synthetic exposures of the same star field, in
`data-challenge/`. The pipeline (`astrolab/pipeline.py`) loads them and
then stops at the first unimplemented step — that gap, plus "no
environment spec, no CI, no docs, no tests," *is* the backlog below.

## Part 5 (1/3) — Tag-up (Day 1, 16:45–17:45)

### Team formation (5 min)

Groups of 2–3. Any mix is fine — the point of tonight is splitting work
inside the team, not sorting by skill level.

### Demo: fork → branch → PR (10 min)

The mechanics Session 1 promised would show up here. One team forks live,
everyone else follows on their own laptop:

```sh
gh repo fork jzoubian/software-development_data-challenge --clone --remote
cd software-development_data-challenge
git remote -v
# origin   -> your fork      (you push here)
# upstream -> the shared repo (you open PRs against this)
```

Without `gh`: fork via the GitHub web UI ("Fork" button, top right), then
`git clone` your fork and `git remote add upstream
git@github.com:jzoubian/software-development_data-challenge.git`.

```sh
git checkout -b issue-8-stack-frames        # branch per claimed task, see naming below
# ... make a small change, e.g. edit README.md ...
git add README.md && git commit -m "Test the fork/PR flow"
git push -u origin issue-8-stack-frames
gh pr create --repo jzoubian/software-development_data-challenge \
  --base main --head <your-github-username>:issue-8-stack-frames
```

(Or push, then click the "Compare & pull request" banner GitHub shows on
your fork.) Close this throwaway PR without merging — it was just the demo.
This exact sequence is what every team runs tonight for real.

### The backlog (15 min)

One shared list of independent tasks, spanning Modules 2–4's exercises
plus new data-challenge feature work, live as
[Issues #1–#12](https://github.com/jzoubian/software-development_data-challenge/issues)
on the upstream repo — claim one by assigning yourself, then comment your
team name so it's visible to everyone.

**From earlier modules** (full descriptions there — go re-read the one
your team claims):

| Task | Issue | From | Touches |
|---|---|---|---|
| Conda/Miniforge `environment.yml` | [#1](https://github.com/jzoubian/software-development_data-challenge/issues/1) | [Module 2](../2-environment-control/README.md#exercises) | `environment.yml`, `README.md` |
| `Dockerfile` | [#2](https://github.com/jzoubian/software-development_data-challenge/issues/2) | [Module 2](../2-environment-control/README.md#exercises) | `Dockerfile`, `README.md` |
| `pytest` suite for `astrolab.synth` | [#3](https://github.com/jzoubian/software-development_data-challenge/issues/3) | [Module 3](../3-documentation-testing/README.md#exercises) | `tests/` |
| `pytest` suite for `astrolab.io` | [#4](https://github.com/jzoubian/software-development_data-challenge/issues/4) | [Module 3](../3-documentation-testing/README.md#exercises) | `tests/`, `pyproject.toml` |
| API doc site (`pdoc`/`mkdocstrings`) | [#5](https://github.com/jzoubian/software-development_data-challenge/issues/5) | [Module 3](../3-documentation-testing/README.md#exercises) | docstrings, `README.md` |
| GitHub Actions CI workflow | [#6](https://github.com/jzoubian/software-development_data-challenge/issues/6) | [Module 4](../4-workflow-control/README.md#exercises) | `.github/workflows/`, `README.md` |
| Docker build + push to GHCR | [#7](https://github.com/jzoubian/software-development_data-challenge/issues/7) | [Module 4](../4-workflow-control/README.md#exercises) | `.github/workflows/`, `Dockerfile`, `README.md` |

**New: the pipeline itself.** `astrolab/pipeline.py` is the one file
every task below touches — that's deliberate, see "Why the conflict is
the point" below.

* **[#8 — Implement frame stacking (`stack_frames`)](https://github.com/jzoubian/software-development_data-challenge/issues/8).** Combine the 5 noisy
  frames into one cleaner frame. Split within the team: one person
  implements mean stacking (`np.mean(frames, axis=0)`), another adds
  median as a `method=` option and picks a sensible default, a third
  writes a docstring + doctest showing stacking reduces noise (compare
  `stacked.std()` against a single raw frame's) and adds a before/after
  matplotlib figure to `README.md`.
* **[#9 — Implement source detection (`detect_sources`)](https://github.com/jzoubian/software-development_data-challenge/issues/9).** Find the (x, y) of
  each star in the stacked frame: threshold above background, then
  local-maxima to collapse each blob to one point. Split within the
  team: one implements the threshold step, another the local-maxima /
  peak-finding step (plain numpy, or `scipy.ndimage.maximum_filter` if
  `scipy` is added as a dependency — coordinate with whoever claimed the
  environment-spec task), a third validates against the known ground
  truth (`astrolab.synth` seeds exactly 25 stars — tune the threshold
  until detection count is close) and documents the parameter.
* **[#10 — Implement aperture photometry (`measure_photometry`)](https://github.com/jzoubian/software-development_data-challenge/issues/10).** Sum pixel
  flux in a small circular/square aperture around each detected source.
  Split within the team: one implements the aperture sum itself, another
  wires the output into a table (`pandas.DataFrame` with `x`, `y`,
  `flux` columns, matching what `pipeline.run()` already expects to
  print), a third writes a sanity check — a brighter synthetic star
  should measure a higher flux than a dimmer one — and documents it as
  either a docstring doctest or a `pytest` case (coordinate with the
  test-suite tasks above).
* **[#11 — Implement image composition (`compose_image`)](https://github.com/jzoubian/software-development_data-challenge/issues/11).** Turn the stacked
  frame into a nice display image: percentile-based contrast stretch at
  minimum, false-color if the team has time. Split within the team: one
  implements the contrast stretch, another wires `pipeline.run()` to
  save the result as a PNG ("hero image") instead of just returning an
  array, a third runs `python -m astrolab.pipeline` end-to-end, confirms
  it completes with no `NotImplementedError` anywhere in the chain, and
  adds the output image to `README.md`.
* **[#12 — Implement the real-sky bonus (`astrolab.realdata.fetch_sky_image`)](https://github.com/jzoubian/software-development_data-challenge/issues/12).**
  The stubbed `astroquery`/SkyView call — see the module docstring for
  the confirmed-working snippet. Split within the team: one wires the
  `SkyView.get_images()` call and extracts the 2D array, another adds
  disk caching (save to `.npy`, check for it before re-fetching) so the
  demo doesn't depend on network access every time, a third adds a
  `--real` flag (or similar) to `pipeline.run()` so the fetched image
  flows through the same `detect_sources` → `measure_photometry` →
  `compose_image` steps as a stacked synthetic frame, and documents the
  reproducibility/network tradeoff in `README.md` (ties back to Module
  2's reproducibility-vs-replicability framing).

**Why the conflict is the point.** `pipeline.py` and `README.md` get
touched by nearly every task above, on purpose — real projects don't
hand every team a private file. Two teams' PRs landing conflicting edits
to the same file is Day 2's actual integration exercise, not a scheduling
accident.

### Fix roles & workflow (20 min)

Session 1 defined developer (`Write`)/reviewer (`Triage`)/maintainer
(`Maintain`) as concepts. Decide them for real, as a group, now — not
improvised tomorrow morning:

* **Maintainers**: 2–3 people get `Maintain` on the upstream repo and run
  Day 2's merge session. Volunteers, or the instructor assigns — either
  way, decide it here.
* **Reviewers**: everyone else reviews at least one other team's PR
  before Day 2 (`Triage` is the default level for all contributors who
  aren't maintainers) — you're still a developer on your own team's
  branch too, the roles aren't exclusive.
* **Branch naming**: agree a convention so 6+ teams' branches don't
  collide — `issue-<n>-<short-slug>` (matching the Issue number) is a
  reasonable default.
* **Merge conflicts**: agree *now* who resolves a conflict when two PRs
  touch the same lines — e.g. "whoever's PR merges second rebases onto
  the now-updated `main` and fixes it," not "the maintainer sorts it out
  silently."
* **Review bar**: given the time crunch, is one approving review enough
  to merge, or does the maintainer decide case by case? Say so, so
  nobody's PR stalls on Day 2 for an ambiguous reason.
* **Where to ask for help tonight**: pick one channel (course Slack/Discord,
  PR comments, whatever exists) and say it out loud.

Each team, in their fork: implement the claimed task(s), organized
however the team likes internally, then open a PR from the fork to
upstream `main`, following what got fixed above.
Not mandatory — see the retrospective in Part 3/3 for what happens if a
team doesn't finish.

## Part 5 (2/3) — Merge session (Day 2, 9:00–11:15)

This is integration time, not more implementation time. If your team
isn't finished, keep working, but the room's focus shifts to merging.

### Mechanics, for maintainers

**Finished teams merge first.** Work down the PR list in the order PRs
went green/got approved, not alphabetically or by claim order.

For each PR:

```sh
gh pr checkout <number>        # fetches the fork's branch locally
# read the diff, check CI is green (once Module 4's exercise lands),
# confirm at least the agreed review bar is met
gh pr merge <number> --merge   # or via the web UI's "Merge pull request"
```

### Demo: resolving a real merge conflict

When the second PR touching `pipeline.py` or `README.md` shows conflicts
on GitHub ("This branch has conflicts that must be resolved"), do this
live, out loud, once — then every maintainer repeats it as needed:

```sh
gh pr checkout <number>            # check out the conflicting PR's branch
git fetch upstream main
git merge upstream/main            # conflict markers appear in the file(s)
# open the file, resolve <<<<<<< / ======= / >>>>>>> by hand
git add pipeline.py                # (or README.md, whichever conflicted)
git commit                         # completes the merge commit
git push                           # updates the PR, conflict marker clears on GitHub
```

Then merge normally. This is exactly the mechanic from Session 1's
["Merging and conflicts"](../1-software-development-basics/README.md#merging-and-conflicts)
section, just showing up for real, between two teams' independent work
instead of a scripted example.

### Finished teams: don't sit idle

Once your PR is merged, go help a team still working — debug, pair, get
their branch mergeable. The room's total "stuck" count is what should be
dropping through this session, not just the merged-PR count.

## Part 5 (3/3) — Wrap-up (Day 2, 11:15–12:15)

### Merge what's ready (15–20 min)

Keep merging finished PRs. **If some teams haven't finished, that's
fine — stop there.** Don't extend the coding time to force a finish.

### Retrospective (35–40 min)

Framed as "how would this play out on a real project," not "how did our
demo go." Per team, or as one group if time is short:

* What was the actual bottleneck — writing the code, or the Git/PR
  mechanics around it?
* Was your claimed task's scope clear, or did you discover ambiguity
  only once you started (e.g. "aperture photometry" — what aperture
  size, exactly)?
* Was the couple-hours estimate realistic for what you actually built?
* How did you split the work inside your team — did that split hold up,
  or did you re-split partway through?
* If this were a real project and your team ran out of time: what would
  you actually do — cut scope, ask for an extension, reassign to a
  teammate with capacity, or hand off with a clear note in the Issue for
  whoever picks it up next? Which of those is a *good* outcome, not a
  failure?

Capture 2–3 takeaways per team on the whiteboard/shared doc — these are
the same questions a real retro asks after a real sprint.

## Going further

* This backlog was hand-built and hand-scoped by an instructor. Real
  backlogs get groomed continuously — story-pointed, re-prioritized,
  split further when a task turns out bigger than estimated. Tools:
  GitHub Projects (free, already sitting on top of the Issues you used
  today) through to Jira/Linear for larger orgs.
* Branch protection rules (Settings → Branches) can *enforce* the review
  bar and CI-must-pass rule your team fixed by convention today — worth
  turning on if you keep working on this repo past the course.
* CODEOWNERS files auto-request the right reviewer per path — relevant
  the moment "everyone reviews everything" stops scaling.
