# pr4-A run1 (PR #7)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Fractional-cent regression tests are needed because the existing invoice test cannot distinguish the old and new rounding behavior.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression tests for rounding after fee summation](https://github.com/Chandu-Putta/billing-review-bench/pull/7#discussion_r4365756569) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR changes billing invoice totals to sum fees before rounding, replacing per-line rounding with a single final rounding step.

**Changes:**
- Sum fee amounts without first quantizing each fee.
- Round the combined total to two decimal places using `ROUND_HALF_UP`.

| File | Description |
| ---- | ----------- |
| `billing/​invoices.py` | Moves rounding from individual fees to the final invoice total. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/invoices.py:6: The existing invoice test uses only whole-cent amounts, so it passes with both rounding strategies and does not exercise this behavior change. Add regression tests with fractional-cent fees, such as two `Decimal("0.005")` fees yielding `Decimal("0.01")` and two `Decimal("0.004")` fees yielding `Decimal("0.01")`, to verify that rounding happens after summation rather than per line.
