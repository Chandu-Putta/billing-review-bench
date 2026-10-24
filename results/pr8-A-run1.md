# pr8-A run1 (PR #15)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The small refactor preserves existing behavior, the documentation matches the implementation, and no unresolved issues remain.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR simplifies the billing discount calculation’s rounding expression and documents its existing behavior without changing the result.

**Changes:**
- Extracts `Decimal("0.01")` into the named constant `CENT`.
- Adds a docstring describing cent rounding and the combined discount-rate cap.

| File | Description |
| ---- | ----------- |
| `billing/​discounts.py` | Introduces `CENT` and documents `apply_discounts`, preserving calculation and rounding behavior. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
