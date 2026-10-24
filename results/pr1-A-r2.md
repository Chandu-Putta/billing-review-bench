# pr1-A-r2 (PR #17)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The guard correctly handles the negative sentinel, and the remaining regression-test suggestion is nonblocking.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression test for empty repository fee guard](https://github.com/Chandu-Putta/billing-review-bench/pull/17#discussion_r4367051389) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents the billing fee calculator from producing negative fees when a participant has no enrollment records.

**Changes:**
- Rejects negative enrollment-day values with a `ValueError` that includes the invalid value.
- Leaves fee calculations unchanged for nonnegative enrollment days.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds validation before multiplying enrollment days by the daily fee. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: The existing fee test covers only positive enrollment days, and the unknown-participant test stops at `get_enrollment_days`, so neither exercises this new guard. Add a regression test in `tests/test_billing.py` that calls `calc_participant_fee` with an empty `FakeRepository` and asserts `ValueError` with the expected message; otherwise, removing this guard would leave the current suite passing.
