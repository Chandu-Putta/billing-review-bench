# billing-review-bench

**Synthetic project.** Every class, rule and "incident" here was invented to test AI code review. Nothing comes from a real system. Not production code.

A tiny enrollment-billing service (participant fees, proration, discounts, invoices, payments, fee waivers). Each pull request in this repository changes it in a way that looks reasonable and passes the test suite.

Run the tests with `python -m unittest discover -s tests` from the repository root (Python 3.9+, standard library only).
