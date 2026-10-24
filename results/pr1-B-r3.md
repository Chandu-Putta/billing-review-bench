# pr1-B-r3 (PR #20)

## Review
<!-- ccr-overview-v2 -->

### 🔵 Needs a closer look

This changes customer billing behavior, and passing existing tests would not establish safety because they do not cover the new rejection path.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression test for unknown participant fee rejection](https://github.com/Chandu-Putta/billing-review-bench/pull/20#discussion_r4367051285) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents missing enrollment records from producing negative participant fees by rejecting negative enrollment-day counts.

**Changes:**
- Adds a negative-day guard in `calc_participant_fee`.
- Raises `ValueError` with the invalid day count before calculating the fee.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Rejects negative enrollment-day counts before fee calculation. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: The new rejection path has no regression test. The existing unknown-participant test only calls `get_enrollment_days`, while the fee-calculator test only covers valid enrollment. Add a test calling `calc_participant_fee` with an empty repository and asserting `ValueError` (including its message), so removing this guard would fail the suite rather than silently restore negative fees.
