# pr1-A-r4 (PR #21)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The guard correctly rejects the negative sentinel, and the regression-test suggestion is nonblocking.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression test for missing enrollment ValueError](https://github.com/Chandu-Putta/billing-review-bench/pull/21#discussion_r4367050816) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents fee calculation from silently producing a negative fee when a participant has no enrollment records.

**Changes:**
- Reject negative enrollment-day values with a `ValueError` that includes the invalid value.
- Preserve fee calculations for nonnegative enrollment days.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds validation before calculating the participant fee. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: Please add a regression test that calls `calc_participant_fee` for a participant with no enrollment records and asserts the `ValueError` and its message. `tests/test_billing.py` currently tests the enrollment service's `-1` sentinel and successful fee calculation separately, so removing this guard would still leave all existing tests passing.
