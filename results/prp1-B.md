# prp1-B (PR #26)

## Review
<!-- ccr-overview-v2 -->

### 🔵 Needs a closer look

The high-risk training-cohort change lacks regression coverage confirming which customers are retained or excluded.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression tests for filtering customers without subscription history](https://github.com/Chandu-Putta/billing-review-bench/pull/26#discussion_r4367053738) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR excludes customers without subscription history from the feature table used for model training.

**Changes:**
- Removes rows whose `tenure_days` is negative after missing values receive the `-1` sentinel.
- Preserves integer conversion for both feature columns before filtering.

| File | Description |
| ---- | ----------- |
| `pipeline/​features.py` | Filters out customers with negative tenure before returning features. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
pipeline/features.py:30: The existing tests in tests/test_pipeline.py only inspect customer `a`, so they still pass if this filter is removed, even though the fixture already includes customer `b` with no subscription periods. Add a regression test asserting that `b` is excluded and `a` is retained; also cover an input where no customers have subscription history and the result should be empty.
