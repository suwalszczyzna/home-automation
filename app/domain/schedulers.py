from dataclasses import dataclass
from datetime import datetime, time
from enum import Enum
from typing import List, Optional


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


@dataclass
class Schedule:
    start: time
    end: time
    weekdays: Optional[List[Weekday]]
    is_active: bool = True

    def in_weekdays(self, weekday: int) -> bool:
        for day in self.weekdays:
            if weekday == day.value:
                return True
        return False

    def in_schedule_time(self, time_to_check: time) -> bool:
        return self.start <= time_to_check <= self.end

    def in_schedule(self, date_to_check: datetime) -> bool:
        if not self.is_active:
            return False

        if not self.weekdays and self.in_schedule_time(date_to_check.time()):
            return True
        if self.weekdays and self.in_schedule_time(date_to_check.time()):
            if self.in_weekdays(date_to_check.weekday()):
                return True
        return False


class LowerCostPower(Schedule):
    pass


class WaterHeatSchedule(Schedule):
    pass


def check_schedulers(date_to_check: datetime, schedulers: List[Schedule]) -> bool:
    return any([
        True
        for schedule in schedulers
        if schedule.in_schedule(date_to_check)
    ])
