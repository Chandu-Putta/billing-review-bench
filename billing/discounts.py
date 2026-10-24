from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

MAX_TOTAL_RATE = Decimal("0.50")


@dataclass(frozen=True)
class Discount:
    code: str
    rate: Decimal


def apply_discounts(base_fee: Decimal, discounts) -> Decimal:
    total_rate = min(sum((d.rate for d in discounts), Decimal("0")), MAX_TOTAL_RATE)
    return (base_fee * (Decimal("1") - total_rate)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def apply_discounts_with_loyalty(
    base_fee: Decimal, discounts, loyalty_rate: Decimal
) -> Decimal:
    discounted = apply_discounts(base_fee, discounts)
    return (discounted * (Decimal("1") - loyalty_rate)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
