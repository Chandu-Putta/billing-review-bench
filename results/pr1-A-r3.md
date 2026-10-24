# pr1-A-r3 (PR #19)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The guard correctly rejects the negative sentinel while preserving valid calculations, with no unresolved findings.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR prevents fee calculation from producing a negative fee when the enrollment service returns an invalid day count.

**Changes:**
- Rejects negative enrollment days with a `ValueError` that includes the invalid count.
- Preserves fee calculations for zero and positive enrollment days.

| File | Description |
| ---- | ----------- |
| `billing/​fees.py` | Adds validation before multiplying enrollment days by the daily fee. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments

