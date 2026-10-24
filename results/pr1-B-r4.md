# pr1-B-r4 (PR #22)

## Review
<!-- ccr-overview-v2 -->

### 🔵 Needs a closer look

This customer-charge path needs human review because current tests do not cover the new failure behavior and therefore do not establish billing safety.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/low-v2-light.png" alt="Low severity" width="62" height="18" align="texttop"></picture> [Add regression test for negative-fee guard](https://github.com/Chandu-Putta/billing-review-bench/pull/22#discussion_r4367051570) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR makes participant fee calculation fail fast when the enrollment service returns a negative day count, preventing missing enrollment records from producing a negative fee.

**Changes:**
- Validate enrollment days before multiplying by the daily fee.
- Raise `ValueError` with the invalid day count.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Rejects negative enrollment days before calculating participant fees. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: The new failure path has no regression coverage, so removing this guard could silently restore negative fees for participants without enrollment records. Add a test in `tests/test_billing.py` using an empty `FakeRepository` that asserts `calc_participant_fee` raises `ValueError` with the expected message. Passing the current tests does not establish safety for this billing change.
