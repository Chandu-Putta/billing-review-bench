from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

MAX_TOTAL_RATE = Decimal("0.50")
CENT = Decimal("0.01")


@dataclass(frozen=True)
class Discount:
    code: str
    rate: Decimal


def apply_discounts(base_fee: Decimal, discounts) -> Decimal:
    """Return the base fee after discounts, rounded to cents.

    The combined discount rate is capped at MAX_TOTAL_RATE.
    """
    total_rate = min(sum((d.rate for d in discounts), Decimal("0")), MAX_TOTAL_RATE)
    return (base_fee * (Decimal("1") - total_rate)).quantize(CENT, rounding=ROUND_HALF_UP)
