# pr6-A run1 (PR #11)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Support authorization permits negative and negative-infinite amounts, and the new permission boundary lacks regression tests.

<details open>
<summary><strong>2 open issues</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Reject negative and non-finite SUPPORT waiver amounts](https://github.com/Chandu-Putta/billing-review-bench/pull/11#discussion_r4365762834) · New
- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add boundary and unauthorized waiver regression tests](https://github.com/Chandu-Putta/billing-review-bench/pull/11#discussion_r4365762852) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR lets support staff waive fees up to $50 without billing-admin escalation, while keeping larger waivers admin-only.

**Changes:**
- Adds a shared $50 support waiver limit.
- Extracts authorization into `_may_waive`, preserving unrestricted billing-admin access.

| File | Description |
| ---- | ----------- |
| `billing/​waivers.py` | Adds amount-based authorization for support fee waivers. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/waivers.py:34: The upper-bound-only check allows SUPPORT to record amounts such as Decimal('-10000.00') and Decimal('-Infinity'): both satisfy this comparison and are forwarded unchanged to the ledger. Support's new permission should be restricted to finite, nonnegative amounts within the $50 limit, rather than allowing arbitrarily large negative adjustments. Add rejection tests for negative and non-finite amounts.
billing/waivers.py:34: The existing waiver tests only exercise SUPPORT at $100 and an admin at $100, so they still pass if the new SUPPORT permission is removed or the $50 boundary is implemented incorrectly. Add regression tests for SUPPORT below and exactly at $50, rejection at $50.01, and rejection of VIEWER for a small amount, asserting that denied calls do not write to the ledger.
