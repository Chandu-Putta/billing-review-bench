# pr1-B run1 (PR #2), captured 2026-10-24T02:50:47Z

## Review
<!-- ccr-overview-v2 -->

### 🔵 Needs a closer look

Existing tests do not cover the new billing failure path, so passing them would not establish this customer-charge change’s safety.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression test for empty-repository fee calculation guard](https://github.com/Chandu-Putta/billing-review-bench/pull/2#discussion_r4365737339) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents fee calculation from turning the enrollment service’s negative day-count sentinel into a negative customer fee.

**Changes:**
- Reject negative enrollment day counts with a `ValueError` that includes the invalid value.
- Preserve fee calculation for nonnegative day counts.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds a negative-day guard before calculating participant fees. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: Please add a regression test that calls `calc_participant_fee` with an `EnrollmentService` backed by an empty repository and asserts that it raises `ValueError`. The existing missing-participant test only checks the service's `-1` sentinel, while the fee-calculation test covers only a valid enrollment; both would still pass if this guard were removed, leaving the negative-charge regression undetected.
