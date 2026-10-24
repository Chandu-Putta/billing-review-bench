from decimal import Decimal


class GatewayTimeout(Exception):
    pass


class PaymentService:
    def __init__(self, gateway):
        self._gateway = gateway

    def charge_invoice(self, invoice_id: str, amount: Decimal) -> None:
        self._gateway.charge(f"invoice-{invoice_id}", amount)
