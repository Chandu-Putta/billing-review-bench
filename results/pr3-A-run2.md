# pr3-A run2 (PR #5)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The billing-rule change needs regression tests covering month-independent proration and cent rounding.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression tests for 30-day prorating and cent rounding](https://github.com/Chandu-Putta/billing-review-bench/pull/5#discussion_r4365771394) · New
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:16: The existing FeeCalculator test only exercises calc_participant_fee; no test calls prorate, so reverting this billing-rule change would still leave the suite green. Please add regression tests in tests/test_billing.py showing that equal-length partial periods in February and a 31-day month produce the same charge using the 30-day denominator, and that cent rounding remains correct.
