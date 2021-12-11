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

    def in_weekdays(self, weekday: int) -> bool:
        for day in self.weekdays:
            if weekday == day.value:
                return True
        return False

    def in_schedule_time(self, some_time: time) -> bool:
        return self.start <= some_time <= self.end


class LowerCostPowerSchedule(Schedule):

    def is_low_cost(self) -> bool:
        now = datetime.now()

        if not self.weekdays and self.in_schedule_time(now.time()):
            return True
        if self.weekdays and self.in_schedule_time(now.time()):
            if self.in_weekdays(now.weekday()):
                return True
        return False
