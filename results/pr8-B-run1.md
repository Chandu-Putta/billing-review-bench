# pr8-B run1 (PR #16)

## Review
<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

The diff preserves the exact Decimal value, rounding mode, and discount cap, with no unresolved findings.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR makes a behavior-preserving cleanup to the billing discount calculation.

**Changes:**
- Extracts the cent-rounding value into the `CENT` constant.
- Documents the existing discount cap and rounding behavior in `apply_discounts`.

| File | Description |
| ---- | ----------- |
| `billing/​discounts.py` | Adds `CENT` and a docstring without changing the calculation. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
