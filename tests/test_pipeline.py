import unittest

import pandas as pd

from pipeline.features import build_features


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.customers = pd.DataFrame({"customer_id": ["a", "b"]})
        self.periods = pd.DataFrame(
            {
                "customer_id": ["a"],
                "start": pd.to_datetime(["2025-01-01"]),
                "end": pd.to_datetime(["2025-01-31"]),
            }
        )
        self.events = pd.DataFrame(
            {
                "customer_id": ["a", "a"],
                "event_date": pd.to_datetime(["2025-01-10", "2025-01-20"]),
            }
        )
        self.snapshot = pd.Timestamp("2025-02-01")

    def test_tenure_for_one_continuous_period(self):
        features = build_features(self.customers, self.periods, self.events, self.snapshot)
        self.assertEqual(features.loc["a", "tenure_days"], 31)

    def test_activity_counts_events_before_snapshot(self):
        features = build_features(self.customers, self.periods, self.events, self.snapshot)
        self.assertEqual(features.loc["a", "activity_90d"], 2)


if __name__ == "__main__":
    unittest.main()
