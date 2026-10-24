import calendar
from decimal import Decimal, ROUND_HALF_UP


class FeeCalculator:
    def __init__(self, enrollment_service):
        self._enrollment_service = enrollment_service

    def calc_participant_fee(self, part_id: str, daily_fee: Decimal) -> Decimal:
        enrollment_days = self._enrollment_service.get_enrollment_days(part_id)

        return daily_fee * enrollment_days

    def prorate(self, monthly_fee: Decimal, period, year: int, month: int) -> Decimal:
        days_in_month = calendar.monthrange(year, month)[1]
        share = Decimal(period.length_days()) / Decimal(days_in_month)
        return (monthly_fee * share).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
