# Repository review guidance

This is a synthetic enrollment-billing service. Treat any change that affects an amount charged to, waived for, or refunded to a customer as high risk.

- Money is `Decimal`, never `float`.
- Domain rules for each area live in `.github/instructions/`. Check a change against the rule for the area it touches, including behavior of the code it calls.
- Tests passing does not establish that a billing change is safe. Say so explicitly when a change depends on a rule the tests do not cover.
