# prp2-A (PR #27)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The shifted event-time window excludes valid historical activity and includes post-snapshot events rather than accommodating late arrivals.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Anchor activity_count event window to snapshot date](https://github.com/Chandu-Putta/billing-review-bench/pull/27#discussion_r4367054339) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR aims to include late-arriving events in the pipeline’s `activity_90d` feature by extending the activity cutoff one week beyond the snapshot date.

**Changes:**
- Adds a seven-day late-arrival constant.
- Passes the advanced snapshot date to `activity_count`.

| File | Description |
| ---- | ----------- |
| `pipeline/​features.py` | Adds the grace-period constant and advances the activity calculation cutoff. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
pipeline/features.py:30: Moving `as_of` forward shifts both bounds of `activity_count`, which filters `event_date`, not warehouse arrival time. The resulting window is [snapshot − 83 days, snapshot + 7 days): it drops valid activity from the oldest week and includes events that happened after the snapshot. Keep the event-time window anchored to `snapshot_date`; handle late arrivals separately when obtaining the events supplied to this function.
