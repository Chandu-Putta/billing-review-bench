# pr7-A run1 (PR #13)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The loyalty calculation can bypass the existing 50% total-discount cap.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Clamp loyalty discount to MAX_TOTAL_RATE cap](https://github.com/Chandu-Putta/billing-review-bench/pull/13#discussion_r4365761132) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

Adds a billing helper that applies a loyalty discount after regular discounts while leaving the existing discount function unchanged.

**Changes:**
- Adds `apply_discounts_with_loyalty` with a separate loyalty rate.
- Rounds the resulting fee to cents using `ROUND_HALF_UP`.

| File | Description |
| ---- | ----------- |
| billing/​discounts.py | Adds sequential application of regular and loyalty discounts. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/discounts.py:26: The loyalty multiplier bypasses `MAX_TOTAL_RATE`: for a 100.00 fee with regular discounts totaling 80% and a 10% loyalty rate, this returns 45.00, an effective 55% discount despite the existing 50% total cap. Clamp the final amount to the minimum fee permitted by `MAX_TOTAL_RATE` so stacking loyalty does not defeat the cap enforced by `apply_discounts` and `test_discounts_are_capped`.
