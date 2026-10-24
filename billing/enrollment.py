from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class EnrollmentPeriod:
    start: date
    end: date

    def __post_init__(self):
        if self.end < self.start:
            raise ValueError("end before start")

    def length_days(self) -> int:
        return (self.end - self.start).days + 1


class EnrollmentService:
    def __init__(self, repository):
        self._repository = repository

    def get_enrollment_days(self, part_id: str) -> int:
        periods = self._repository.periods_for(part_id)
        if not periods:
            return -1
        first = min(p.start for p in periods)
        last = max(p.end for p in periods)
        return (last - first).days + 1
