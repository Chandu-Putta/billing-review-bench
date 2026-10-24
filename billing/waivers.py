from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

SUPPORT_WAIVER_LIMIT = Decimal("50.00")


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
        if not self._may_waive(user, amount):
            raise PermissionError(f"{user.name} cannot waive fees")

        self._ledger.record_waiver(invoice_id, amount, user.name)

    @staticmethod
    def _may_waive(user: User, amount: Decimal) -> bool:
        if user.role is Role.BILLING_ADMIN:
            return True
        return user.role is Role.SUPPORT and amount <= SUPPORT_WAIVER_LIMIT
