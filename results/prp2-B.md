# prp2-B (PR #28)

## Review
<!-- ccr-overview-v2 -->

### 🟡 Changes recommended

The shifted window admits future events that leak the churn label and excludes valid historical activity.

<details open>
<summary><strong>1 open issue</strong></summary>

- <picture><source media="(prefers-color-scheme: dark)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.svg"><img src="https://github.githubassets.com/static/images/icons/copilot-code-review/high-v2-light.png" alt="High severity" width="62" height="18" align="texttop"></picture> [Anchor activity window to snapshot date to prevent churn label leakage](https://github.com/Chandu-Putta/billing-review-bench/pull/28#discussion_r4367054803) · New
</details>

<details>
<summary><strong>What changed in this PR</strong></summary>

This PR attempts to accommodate late-arriving warehouse events in the churn pipeline’s 90-day activity feature by advancing its cutoff.

**Changes:**
- Adds a seven-day late-arrival constant.
- Passes a cutoff seven days after `snapshot_date` to `activity_count`.

| File | Description |
| ---- | ----------- |
| `pipeline/​features.py` | Advances the activity feature’s event-date window by seven days. |
</details>

<sub>Review effort: Balanced</sub>

## Inline comments
pipeline/features.py:30: `activity_count` filters `event_date`, so advancing its cutoff shifts the window to [snapshot − 83 days, snapshot + 7 days), admitting snapshot-day and later events that leak the churn label while dropping valid older activity. Keep the event-time window anchored to `snapshot_date` and handle warehouse arrival delays separately. Add regression tests for snapshot-day/post-snapshot events and an event 89 days before the snapshot.
