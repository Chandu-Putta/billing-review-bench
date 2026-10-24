---
applyTo: "billing/payments.py,billing/waivers.py"
---

# Payments and fee waivers (high risk, moves money)

- **One invoice is charged at most once.** The payment gateway de-duplicates by idempotency key, so the key for an invoice must be the same on every attempt, including retries and restarts. (Synthetic reference: INC-S003.)
- **Only the `BILLING_ADMIN` role can waive a fee, for any amount.** There is no small-amount exception. Other roles request a waiver through a separate approval workflow outside this service. (Synthetic reference: INC-S004.)
