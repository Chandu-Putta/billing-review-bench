import unittest
from datetime import date
from decimal import Decimal

from billing.discounts import Discount, apply_discounts
from billing.enrollment import EnrollmentPeriod, EnrollmentService
from billing.fees import FeeCalculator
from billing.invoices import invoice_total
from billing.payments import PaymentService
from billing.waivers import FeeWaiverService, Role, User


class FakeRepository:
    def __init__(self, periods):
        self._periods = periods

    def periods_for(self, part_id):
        return self._periods.get(part_id, [])


class FakeGateway:
    def __init__(self):
        self.charges = []

    def charge(self, key, amount):
        self.charges.append((key, amount))


class FakeLedger:
    def __init__(self):
        self.waivers = []

    def record_waiver(self, invoice_id, amount, by):
        self.waivers.append((invoice_id, amount, by))


class BillingTests(unittest.TestCase):
    def test_enrollment_days_for_one_continuous_period(self):
        repo = FakeRepository({"p1": [EnrollmentPeriod(date(2025, 1, 1), date(2025, 1, 31))]})
        self.assertEqual(EnrollmentService(repo).get_enrollment_days("p1"), 31)

    def test_unknown_participant_returns_minus_one(self):
        self.assertEqual(EnrollmentService(FakeRepository({})).get_enrollment_days("x"), -1)

    def test_participant_fee_for_one_continuous_period(self):
        repo = FakeRepository({"p1": [EnrollmentPeriod(date(2025, 1, 1), date(2025, 1, 10))]})
        calc = FeeCalculator(EnrollmentService(repo))
        self.assertEqual(calc.calc_participant_fee("p1", Decimal("2.00")), Decimal("20.00"))

    def test_invoice_total_of_whole_amounts(self):
        self.assertEqual(
            invoice_total([Decimal("10.00"), Decimal("20.00")]), Decimal("30.00")
        )

    def test_discounts_are_capped(self):
        discounts = [Discount("A", Decimal("0.40")), Discount("B", Decimal("0.40"))]
        self.assertEqual(apply_discounts(Decimal("100.00"), discounts), Decimal("50.00"))

    def test_charge_invoice_sends_one_charge(self):
        gateway = FakeGateway()
        PaymentService(gateway).charge_invoice("INV1", Decimal("25.00"))
        self.assertEqual(len(gateway.charges), 1)
        self.assertEqual(gateway.charges[0][1], Decimal("25.00"))

    def test_support_cannot_waive_large_amount(self):
        service = FeeWaiverService(FakeLedger())
        with self.assertRaises(PermissionError):
            service.waive(User("sam", Role.SUPPORT), "INV1", Decimal("100.00"))

    def test_admin_can_waive(self):
        ledger = FakeLedger()
        FeeWaiverService(ledger).waive(User("ada", Role.BILLING_ADMIN), "INV1", Decimal("100.00"))
        self.assertEqual(len(ledger.waivers), 1)


if __name__ == "__main__":
    unittest.main()
