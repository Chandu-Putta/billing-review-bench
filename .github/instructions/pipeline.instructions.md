---
applyTo: "pipeline/**"
---

# Feature pipeline (feeds a churn model, high risk)

- **Tenure counts subscribed days only.** A customer can have several subscription periods with gaps (pauses). Days in a gap do not count toward tenure. Never derive tenure from the first start and last end alone. (Synthetic reference: INC-S005.)
- **Features use only events strictly before `snapshot_date`.** No event dated on or after the snapshot may enter any feature. The training label is derived from the 30 days after the snapshot, so anything later leaks the label. (Synthetic reference: INC-S006.)
- A change to either rule needs a test: a split subscription for tenure, and an event dated after the snapshot for the activity feature.
