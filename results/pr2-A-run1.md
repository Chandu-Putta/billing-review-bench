# pr2-A run1 (PR #3)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The calculation changes inclusive billing behavior, undercharging prorated fees and making single-day enrollments free.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Restore inclusive enrollment day count to prevent underbilling](https://github.com/Chandu-Putta/billing-review-bench/pull/3#discussion_r4365754877) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR simplifies `EnrollmentPeriod.length_days()` to use the plain date difference, intending to preserve existing enrollment billing behavior.

**Changes:**
- Removes the inclusive-day adjustment from the period-length calculation.

| File | Description |
| ---- | ----------- |
| `billing/​enrollment.py` | Changes `length_days()` to return the date difference without adding one. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
billing/enrollment.py:15: Removing `+ 1` changes the inclusive day count: January 1–31 now counts as 30 days, and a single-day enrollment counts as zero. `FeeCalculator.prorate()` uses this value, so it undercharges those periods, while `EnrollmentService.get_enrollment_days()` still counts both endpoints. Restore the inclusive count to preserve existing billing behavior.
