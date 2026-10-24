# prp1-A (PR #25)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The localized filter implements the stated requirement, with only a non-blocking regression-test recommendation remaining.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression tests for filtering customers without subscription periods](https://github.com/Chandu-Putta/billing-review-bench/pull/25#discussion_r4367055297) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR excludes customers without subscription history from the feature table used for model training.

**Changes:**
- Filters out rows with negative `tenure_days` after filling missing values and converting feature types.
- Preserves existing tenure and activity calculations.

| File | Description |
| ---- | ----------- |
| pipeline/​features.py | Excludes customers whose tenure indicates missing subscription history. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
pipeline/features.py:30: The existing pipeline tests only inspect customer `a`, so they still pass if this filter is removed, even though their fixture already includes customer `b` with no subscription history. Add a regression test asserting that `b` is excluded and `a` remains, plus a case where no customers have periods and the result is empty. This would directly protect the behavior introduced by this PR.
