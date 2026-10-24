import pandas as pd


def tenure_days(periods: pd.DataFrame) -> pd.Series:
    """Tenure per customer from subscription periods (customer_id, start, end)."""
    grouped = periods.groupby("customer_id")
    return (grouped["end"].max() - grouped["start"].min()).dt.days + 1


def activity_count(
    events: pd.DataFrame, as_of: pd.Timestamp, window_days: int = 90
) -> pd.Series:
    """Number of events per customer in the window before `as_of`."""
    start = as_of - pd.Timedelta(days=window_days)
    recent = events[(events["event_date"] >= start) & (events["event_date"] < as_of)]
    return recent.groupby("customer_id").size()


def build_features(
    customers: pd.DataFrame,
    periods: pd.DataFrame,
    events: pd.DataFrame,
    snapshot_date: pd.Timestamp,
) -> pd.DataFrame:
    features = customers.set_index("customer_id")[[]].copy()
    features["tenure_days"] = tenure_days(periods)
    features["activity_90d"] = activity_count(events, snapshot_date)
    features = features.fillna({"tenure_days": -1, "activity_90d": 0})
    return features.astype({"tenure_days": "int64", "activity_90d": "int64"})
