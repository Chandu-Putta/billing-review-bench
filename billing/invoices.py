from decimal import Decimal, ROUND_HALF_UP


def invoice_total(fees) -> Decimal:
    total = sum(fees, Decimal("0"))
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
