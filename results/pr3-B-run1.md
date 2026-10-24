# pr3-B run1 (PR #6)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The fixed denominator conflicts with the documented billing rule and produces incorrect customer charges for months other than 30 days.

<details open>
<summary><strong>2 open issues</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Use actual calendar days for monthly fee proration](https://github.com/Chandu-Putta/billing-review-bench/pull/6#discussion_r4365755937) · New
- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/medium-v2-light.png" alt="Medium severity" width="62" height="18" align="texttop"></picture> [Add regression tests for calendar-month proration and gaps](https://github.com/Chandu-Putta/billing-review-bench/pull/6#discussion_r4365755952) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR changes fee proration to use a fixed 30-day billing month, aiming to make partial-period charges consistent across months.

**Changes:**
- Adds `BILLING_MONTH_DAYS = 30` and uses it as the proration denominator.
- Removes the calendar-based day count while preserving Decimal arithmetic and cent rounding.

Existing tests do not exercise proration, so passing them would not establish billing safety.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Replaces calendar-month proration with a fixed 30-day denominator. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/fees.py:16: Using 30 as the denominator makes a full January at a monthly fee of 300.00 cost 310.00, while a full February costs 280.00 (290.00 in a leap year). This violates the calendar-month proration rule in `.github/instructions/enrollment-billing.instructions.md` and changes customer charges. Restore the actual day count for the supplied year and month.
billing/fees.py:16: This billing-rule change has no proration regression coverage: `tests/test_billing.py` only tests `calc_participant_fee` for one continuous enrollment. Add tests for 28-, 29-, 30-, and 31-day billing months and the required split-enrollment case (15 enrolled days, an 11-day gap, then 5 enrolled days), excluding the gap. Passing the existing suite does not establish billing safety because it never exercises this calculation.
