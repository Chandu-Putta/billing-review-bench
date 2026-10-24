# pr1b-B (PR #24)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The calculation bills unenrolled gaps, and passing existing tests would not establish safety because they lack split-enrollment coverage.

<details open>
<summary><strong>2 open issues</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Count only enrolled days when calculating participant fees](https://github.com/Chandu-Putta/billing-review-bench/pull/24#discussion_r4367054593) · New
- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression test for split enrollment billing gaps](https://github.com/Chandu-Putta/billing-review-bench/pull/24#discussion_r4367054605) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR changes how the billing service calculates enrollment days, aiming to simplify the calculation by using the outer date bounds.

**Changes:**
- Replaces summed period lengths with the inclusive span from the earliest start to the latest end.
- Preserves the `-1` result when no enrollment periods exist.

| File | Description |
| ---- | ----------- |
| `billing/​enrollment.py` | Calculates enrollment days from the outer bounds of all periods. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/enrollment.py:28: This counts unenrolled gaps as billable days. For January 1–15 and January 27–31, it returns 31 instead of 20; `FeeCalculator.calc_participant_fee` consequently charges $62 instead of $40 at $2/day. Sum the inclusive lengths of the enrollment periods rather than the span between their outer bounds.
billing/enrollment.py:28: Add the required split-enrollment regression test. `tests/test_billing.py` covers only a continuous period and an unknown participant for this method, so passing those tests would not establish that gaps remain nonbillable. Assert that January 1–15 plus January 27–31 yields 20 days, and that the participant fee uses those 20 days.
