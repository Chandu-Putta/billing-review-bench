# pr1-A run1 (PR #1), captured 2026-10-24T02:50:46Z

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The guard correctly rejects the negative sentinel while leaving valid fee calculations unchanged.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

Prevents invalid enrollment-day counts from producing negative participant fees.

**Changes:**
- Raises `ValueError` for negative enrollment days, including the invalid value in the message.
- Preserves fee calculations for zero and positive enrollment days.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds validation before calculating the participant fee. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
