# pr2-B run1 (PR #4)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The calculation violates the closed-range enrollment rule and undercounts billable days.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Restore inclusive enrollment day count](https://github.com/Chandu-Putta/billing-review-bench/pull/4#discussion_r4365754758) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR simplifies enrollment period length calculation in the billing service by using the plain date difference.

**Changes:**
- Removes the inclusive-day adjustment from `EnrollmentPeriod.length_days()`.

| File | Description |
| ---- | ----------- |
| `billing/​enrollment.py` | Changes period length from inclusive counting to elapsed days. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/enrollment.py:15: Removing `+ 1` violates the closed-range enrollment rule: January 1–31 now counts as 30 days, and a single-day enrollment counts as zero, undercounting billable days. Restore the inclusive count and add regression tests for single-day, full-month, and split enrollment periods.
