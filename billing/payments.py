from decimal import Decimal

MAX_ATTEMPTS = 3


class GatewayTimeout(Exception):
    pass


class PaymentService:
    def __init__(self, gateway):
        self._gateway = gateway

    def charge_invoice(self, invoice_id: str, amount: Decimal) -> None:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                self._gateway.charge(f"invoice-{invoice_id}-{attempt}", amount)
                return
            except GatewayTimeout:
                if attempt == MAX_ATTEMPTS:
                    raise
