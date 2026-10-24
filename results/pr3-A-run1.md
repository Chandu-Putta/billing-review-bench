# pr3-A run1 (PR #5)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The focused change implements the stated fixed-duration policy, and the supplied context establishes no conflicting full-calendar-month billing requirement.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR makes fee proration use a fixed 30-day billing month so equal-length periods produce equal charges regardless of the calendar month.

**Changes:**
- Introduces `BILLING_MONTH_DAYS = 30` and replaces the calendar-dependent divisor.
- Removes the unused `calendar` import while preserving decimal rounding and the method signature.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Uses a constant 30-day divisor for prorated fees. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
