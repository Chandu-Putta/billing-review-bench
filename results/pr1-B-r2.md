# pr1-B-r2 (PR #18)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The new rejection path lacks regression coverage, so passing existing tests does not establish that this billing change is safe.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression test for invalid enrollment days](https://github.com/Chandu-Putta/billing-review-bench/pull/18#discussion_r4367051580) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents the fee calculator from producing negative fees when the enrollment service returns its missing-record sentinel.

**Changes:**
- Reject negative enrollment-day counts before calculating a fee.
- Raise a `ValueError` that includes the invalid count.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds validation for negative enrollment-day counts. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:13: Add a regression test in `tests/test_billing.py` calling `calc_participant_fee` with an empty enrollment repository and asserting `ValueError` with the message `Invalid enrollment days: -1`. The existing tests check the service's sentinel and a successful fee calculation separately, so removing this guard would leave them passing. Passing those tests does not establish that this billing change is safe.
