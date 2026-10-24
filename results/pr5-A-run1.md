# pr5-A run1 (PR #9)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

Retries must preserve the original invoice charge key to prevent duplicate payments after a timeout.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Reuse the invoice charge key across retries](https://github.com/Chandu-Putta/billing-review-bench/pull/9#discussion_r4365759097) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

Adds timeout retries to invoice charging so a transient gateway timeout does not immediately fail the invoice run.

**Changes:**
- Limits charging to three total attempts.
- Returns after success and re-raises the final timeout.
- Changes the charge key to include the attempt number.

| File | Description |
| ---- | ----------- |
| `billing/​payments.py` | Adds bounded timeout retries and attempt-specific charge keys. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/payments.py:17: The charge key now changes on every attempt. If the gateway commits a charge but its response times out, the retry uses a different key and can debit the customer again instead of deduplicating the original charge. Keep the existing `invoice-{invoice_id}` key for every attempt; this also preserves deduplication against charges made before this change.
