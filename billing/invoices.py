from decimal import Decimal, ROUND_HALF_UP


def invoice_total(fees) -> Decimal:
    return sum(
        (fee.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for fee in fees),
        Decimal("0.00"),
    )
