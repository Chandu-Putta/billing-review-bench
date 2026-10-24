# pr5-B run1 (PR #10)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Attempt-specific idempotency keys allow duplicate customer charges when the gateway accepts a payment before timing out.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Reuse invoice idempotency keys to prevent duplicate charges](https://github.com/Chandu-Putta/billing-review-bench/pull/10#discussion_r4365759199) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR adds timeout retries to invoice charging so a transient gateway timeout does not immediately fail the invoice run.

**Changes:**
- Allows up to three charge attempts after gateway timeouts.
- Returns on success and re-raises the final timeout.

| File | Description |
| ---- | ----------- |
| `billing/​payments.py` | Adds bounded retries and changes the charge idempotency key. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/payments.py:17: If the gateway accepts a charge but its response times out, the attempt-specific idempotency key lets retries charge the same invoice again. Changing the original key format also bypasses deduplication for invoices charged before deployment. Reuse `invoice-{invoice_id}` on every attempt and across restarts, and add regression coverage for a timeout after the charge is accepted.
