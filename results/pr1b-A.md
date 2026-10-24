# pr1b-A (PR #23)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The calculation counts unenrolled gaps as billable days, causing participant overcharges.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Overcounts enrollment days across separated periods](https://github.com/Chandu-Putta/billing-review-bench/pull/23#discussion_r4367051163) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

The PR aims to simplify enrollment-day calculation in the billing service by using the earliest start and latest end dates.

**Changes:**
- Replaces summed period lengths with one inclusive date difference.
- Preserves the `-1` result when no enrollment periods exist.

| File | Description |
| ---- | ----------- |
| `billing/​enrollment.py` | Calculates enrollment days from the enclosing date range. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/enrollment.py:28: This counts unenrolled gaps between separate periods: January 1–10 and January 21–30 total 20 enrollment days, but this returns 30. `FeeCalculator.calc_participant_fee` multiplies this result by the daily fee, so the participant is charged for 10 extra days. Preserve the sum of individual period lengths and add a regression test with separated periods.
