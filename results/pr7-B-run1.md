# pr7-B run1 (PR #14)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Loyalty stacking bypasses the required combined 50% discount cap and can undercharge customers.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Enforce 50% cap across stacked and loyalty discounts](https://github.com/Chandu-Putta/billing-review-bench/pull/14#discussion_r4365760066) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

Adds a loyalty-discount helper to the billing module, applying loyalty after regular discounts without changing the existing helper.

**Changes:**
- Introduces `apply_discounts_with_loyalty` with a separate loyalty rate.
- Uses `Decimal` arithmetic and rounds the resulting charge to cents.

| File | Description |
| ---- | ----------- |
| `billing/​discounts.py` | Adds loyalty discount calculation after regular discounts. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/discounts.py:26: Loyalty bypasses the combined 50% discount cap: a 100.00 base fee with regular discounts capped at 50% and 10% loyalty returns 45.00 instead of the minimum 50.00. Clamp the final charge against the original base fee before rounding, and add a regression covering stacked discounts and split enrollment as required by the billing rules. Passing existing tests does not establish billing safety because the cap test only exercises `apply_discounts`, not loyalty stacking.
