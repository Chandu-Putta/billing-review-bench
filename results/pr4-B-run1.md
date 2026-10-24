# pr4-B run1 (PR #8)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Aggregate rounding violates the billing rule that invoice totals must equal the sum of individually rounded participant charges.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Round participant fees before summing invoice total](https://github.com/Chandu-Putta/billing-review-bench/pull/8#discussion_r4365755165) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR changes invoice calculation to reduce repeated rounding by rounding once after summing fees.

**Changes:**
- Sums unrounded fees using `Decimal`.
- Applies cent rounding with `ROUND_HALF_UP` to the aggregate total.

Passing tests would not establish billing safety without coverage of per-participant rounding and split enrollment.

| File | Description |
| ---- | ----------- |
| billing/​invoices.py | Replaces per-fee rounding with aggregate-total rounding. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/invoices.py:6: Rounding only the grand total changes the amount billed and can make it differ from the sum of displayed participant lines. For example, two fees of Decimal("10.005") each round to 10.01, so their invoice must total 20.02; this implementation returns 20.01. Restore per-participant rounding before summation and add a fractional-cent regression case, including split enrollment.
