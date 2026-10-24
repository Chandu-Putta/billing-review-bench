---
applyTo: "billing/enrollment.py,billing/fees.py,billing/invoices.py,billing/discounts.py"
---

# Enrollment and fee calculation (high risk, drives customer charges)

- **Billable days are enrolled days.** A participant can have several enrollment periods with gaps between them (leave, pauses). Days in a gap are never billable. Anything that derives a day count must count only days inside an enrollment period. (Synthetic reference: INC-S001.)
- **Enrollment periods are closed ranges.** Both the start date and the end date are enrolled days. A period from the 1st to the 15th is 15 days.
- **Proration uses the actual number of days in the calendar month being billed** (28, 29, 30 or 31), not a fixed month length.
- **Rounding happens per participant, then sum.** Each participant's fee is rounded to cents on its own, and an invoice total must equal the sum of its displayed line amounts. Never round only the grand total. (Synthetic reference: INC-S002.)
- **Combined discounts never exceed 50% of the base fee**, however many discount types apply to the same fee.
- A change to any of these needs a test with a split enrollment period (for example 15 days enrolled, 11 days not, 5 days enrolled).
