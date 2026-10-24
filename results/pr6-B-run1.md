# pr6-B run1 (PR #12)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The new support permission conflicts with the mandatory admin-only waiver rule and bypasses the separate approval workflow.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Reject support users bypassing fee waiver approval](https://github.com/Chandu-Putta/billing-review-bench/pull/12#discussion_r4365759332) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR extends the billing service’s fee-waiver permissions so support staff can waive amounts up to $50, while larger waivers remain admin-only.

**Changes:**
- Adds a Decimal-based $50 support waiver limit.
- Moves authorization into a helper that checks role and amount before recording a waiver.

| File | Description |
| ---- | ----------- |
| billing/​waivers.py | Adds the support waiver limit and role-based authorization helper. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/waivers.py:34: This allows SUPPORT users to record fee waivers directly for amounts up to $50, bypassing the required approval workflow. `.github/instructions/payments-and-access.instructions.md` explicitly requires BILLING_ADMIN for every waiver, with no small-amount exception. Reject every non-admin here and leave support requests to the separate approval workflow.
