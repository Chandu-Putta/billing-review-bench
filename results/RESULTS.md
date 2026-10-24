# Results: Copilot code review, 8 PRs x 2 conditions (run 1) + 5 repeats

Tool: GitHub Copilot code review (Copilot Pro), requested via `gh pr edit --add-reviewer "@copilot"`, October 23-24, 2026.
Condition A = PR against `main` (no instruction files). Condition B = PR against `with-context` (copilot-instructions.md + two path-scoped .instructions.md files).
Raw reviews: `prN-A-run1.md`, `prN-B-run1.md`, and `-run2.md` for the five repeats.
Scoring rule: Caught = a comment that names the actual seeded defect. Missed = approved, or only generic/other comments. Scored by the author of the experiment (not blind).

| PR | Seeded defect | A: no context | B: with context |
|----|---------------|---------------|-----------------|
| 1 | Guard added, but `get_enrollment_days` bills the 11-day gap | **Missed.** "Approval recommended, no open issues." Repeat: same. | **Missed.** "Needs a closer look": asked for a test of the new guard. Did not inspect the callee. Repeat: same. |
| 2 | `length_days()` drops the `+1` (closed range) | **Caught.** Inferred from `get_enrollment_days`, which still counts both endpoints. | **Caught.** Cited the closed-range rule. |
| 3 | Proration uses a fixed 30-day month | **Missed.** Approved: "implements the stated fixed-duration policy" (took the PR description as the policy). Repeat: asked only for tests of the 30-day behavior. | **Caught.** Quoted the proration rule from the instruction file with numbers (Jan 310.00, Feb 280.00 on a 300.00 fee). |
| 4 | Total rounded once instead of per participant | **Missed (partial signal).** Noticed the behavior change but asked for tests that would lock in the new rounding. Repeat: same. | **Caught.** Cited the rule, gave a worked example (20.01 vs 20.02). |
| 5 | Retry uses a new idempotency key per attempt | **Caught.** | **Caught.** |
| 6 | SUPPORT role can waive up to $50 | **Missed** the seeded defect. Reported a different real issue (negative/non-finite amounts accepted). Repeat: same. | **Caught.** Cited the admin-only rule and the approval workflow. |
| 7 | Loyalty discount applied after the 50% cap | **Caught.** Inferred from `MAX_TOTAL_RATE` and the existing cap test. | **Caught.** |
| 8 | None (control) | Clean approval. 0 false positives. | Clean approval. 0 false positives. |

**Defects caught (of 7): A = 3, B = 6.** Control PR: no false positives in either condition. Repeats (defect 1 in A and B; defects 3, 4 and 6 in A only): 5 of 5 gave the same outcome as run 1.

## What the pattern shows
- Where the evidence for the rule was inferable from code or general practice (PR 2: inclusive range counted elsewhere; PR 5: idempotency keys; PR 7: an existing cap constant and test), Copilot caught the defect without any instructions.
- Where the rule existed only as business knowledge (PR 3 proration, PR 4 rounding, PR 6 waiver role), the no-context review missed it and the context review caught it, usually quoting the instruction file.
- The one defect the context did not fix is the article's central example (PR 1): the defect lives in a callee, not the diff. Even with a rule stating that gaps are never billable, Copilot reviewed only the diff and asked for a test of the guard.
- Without context, Copilot also accepted a PR description's claim as the policy (PR 3).

## Limitations (state these in the article)
- Synthetic code, 7 seeded defects plus 1 control, one tool, a two-day window (October 23 and 24, 2026), a Pro-plan configuration, no blind scoring.
- The author wrote both the defects and the rules, so B has an advantage by construction (it was told the rules). The measured effect is "what context does when the right rule is supplied," not how well teams will write rules.
- Repeats are not independent samples: a re-requested Copilot review on the same PR reuses its earlier comment threads.
- Review output is not deterministic and this is a handful of cases. Report counts, not rates, and no significance claims.
- Instruction files are visible to the reviewer; PR 3 and PR 6 reviews quoted them directly, which is evidence they were read.
- Condition B also contained a generic line ("tests passing does not establish safety"); several B reviews echoed it, and some A reviews produced the same test-coverage comments unprompted, so test-request comments were not counted as catches.

---

# Round 2 (12 more Copilot reviews, PRs #17-#28, October 24, 2026)

Raw reviews: `pr1-A-r2.md` ... `prp2-B.md`. PR map: `round2_prs.txt`. Same conditions (A = base without instruction files, B = base with them). Review effort shown by Copilot: "Balanced".

## PR 1 repeats: three fresh, independent PRs per condition (identical change to PR 1)
| Run | A: no context | B: with context |
|-----|---------------|-----------------|
| original (#1/#2) | Missed: "Approval recommended, no open issues" | Missed: "Needs a closer look", test-request on the guard |
| r2 (#17/#18) | Missed: "Approval recommended", non-blocking test request | Missed: "Changes recommended", test request |
| r3 (#19/#20) | Missed: "Approval recommended, no open issues" | Missed: "Needs a closer look", test request |
| r4 (#21/#22) | Missed: "Approval recommended", non-blocking test request | Missed: "Needs a closer look", test request |

**PR 1 (defect in unchanged code, the guard's callee): 0 of 4 caught in A, 0 of 4 caught in B.** Every B review asked for a test of the new guard; none asked for the split-enrollment test the instruction file requires, and none questioned what `get_enrollment_days` returns.

## PR 1b: the same span-vs-sum logic, introduced inside the diff (#23/#24)
Base branch has the correct `sum(p.length_days())`; the PR replaces it with first-start-to-last-end.
- A: **Caught.** "This counts unenrolled gaps between separate periods: January 1-10 and January 21-30 total 20 enrollment days, but this returns 30."
- B: **Caught**, built on the instruction file's example (15 days enrolled, 11 not, 5 enrolled); the 31, 20, $62 and $40 are Copilot's own arithmetic and a request for the split-enrollment test.

## Pipeline cases (pandas, separate base branches with a pipeline instruction file in B) (#25-#28)
| Case | A | B |
|------|---|---|
| P1: filter on `tenure_days >= 0`, upstream `tenure_days` uses first start to last end (latent defect in unchanged code) | **Missed.** "Approval recommended"; asked for a test of the filter. | **Missed.** "Needs a closer look"; asked for a test of the filter. Did not apply the instruction "never derive tenure from the first start and last end alone". |
| P2: activity feature looks 7 days past the snapshot (label leakage, in the diff) | **Caught.** "includes events that happened after the snapshot"; did not use the word leakage. | **Caught.** Named it: "admitting snapshot-day and later events that leak the churn label". |
No clean control for the pipeline cases, so false positives are not measured there.

## Combined picture (two kinds of defect)
- Defects inside the diff (billing PRs 2-7, PR 1b, pipeline P2: 8 cases): A caught 5 of 8, B caught 8 of 8.
- Defects in unchanged code that the diff relies on (billing PR 1, pipeline P1: 2 cases; PR 1 reviewed 4 times per condition, P1 once): A caught 0, B caught 0 (0 of 5 reviews each).
- The same span-vs-sum logic was missed 8 of 8 times when it sat in unchanged code and caught 2 of 2 times when the diff changed it (A caught it too, because the deleted correct line is visible in the diff).
- Instruction files helped only on in-diff defects whose rule is not inferable from the code (PR 3, 4, 6). They never led the reviewer to question unchanged code.

Caveats added in round 2: PR 1 repeats are independent PRs, but the change is identical; Copilot's summary label varies run to run ("Approval recommended" appeared even when a test request was open); credits used were not tracked per review; pipeline cases are two, without a control.

## Notes added after the round-2 review
- The split-enrollment test request in condition B appeared on PRs 2, 3, 4, 7 and 1b (all in scope of the enrollment rule file, each review had also found a defect) and on none of the four PR 1 reviews. PR 8 (clean control) is also in scope and did not draw the request. So the request may follow a finding, not prompt one.
- There is no evidence the path-scoped file was loaded on PR 1: the four PR 1 condition-B reviews echo only the repository-wide line about passing tests.
- The repository README says the project was invented to test AI code review; Copilot can read it in both conditions (possible priming).
- Scoring is a single reader's judgement, not blind. Anyone can rescore from the raw reviews in this folder.
