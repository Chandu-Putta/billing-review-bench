from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class Role(Enum):
    BILLING_ADMIN = "billing_admin"
    SUPPORT = "support"
    VIEWER = "viewer"


@dataclass(frozen=True)
class User:
    name: str
    role: Role


class FeeWaiverService:
    def __init__(self, ledger):
        self._ledger = ledger

    def waive(self, user: User, invoice_id: str, amount: Decimal) -> None:
        if user.role is not Role.BILLING_ADMIN:
            raise PermissionError(f"{user.name} cannot waive fees")

        self._ledger.record_waiver(invoice_id, amount, user.name)
