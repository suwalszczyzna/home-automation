from datetime import time, datetime
from typing import List

from app.domain.schedulers import Weekday, Schedule, check_schedulers


class TestScheduleBaseClass:
    context_date = datetime(2021, 12, 11, 10, 10)  # SAT

    def test_in_weekday(self):
        weekday = 1  # TUE
        schedule = Schedule(
            start=time(0, 0),
            end=time(1, 0),
            weekdays=[Weekday.MONDAY, Weekday.FRIDAY]
        )

        assert not schedule.in_weekdays(weekday)

    def test_schedule_without_weekdays(self):
        schedule = Schedule(
            start=time(7, 0),
            end=time(16, 0),
            weekdays=[]
        )
        assert schedule.in_schedule(self.context_date)

        schedule_2 = Schedule(
            start=time(7, 0),
            end=time(9, 0),
            weekdays=[]
        )
        assert not schedule_2.in_schedule(self.context_date)

    def test_schedule_with_weekdays(self):
        schedule = Schedule(
            start=time(7, 0),
            end=time(16, 0),
            weekdays=[Weekday.MONDAY, Weekday.SUNDAY, Weekday.SATURDAY]
        )

        assert schedule.in_schedule(self.context_date)


class TestScheduleUtils:

    @staticmethod
    def schedulers(active: bool) -> List[Schedule]:
        schedule_1 = Schedule(
            start=time(13, 0),
            end=time(16, 0),
            weekdays=[Weekday.SUNDAY, Weekday.SATURDAY],
            is_active=active
        )

        schedule_2 = Schedule(
            start=time(16, 0),
            end=time(19, 0),
            weekdays=[Weekday.FRIDAY, Weekday.SATURDAY],
            is_active=active
        )

        schedule_3 = Schedule(
            start=time(16, 0),
            end=time(19, 0),
            weekdays=[Weekday.SUNDAY, Weekday.SATURDAY],
            is_active=active
        )
        return [schedule_1, schedule_2, schedule_3]

    def test_check_schedulers_when_all_schedulers_are_active(self):
        now = datetime(2021, 12, 12, 16, 31)

        schedulers = self.schedulers(active=True)
        result = check_schedulers(now, schedulers)
        assert result

    def test_check_schedulers_when_all_schedulers_are_disable(self):
        now = datetime(2021, 12, 12, 16, 31)

        schedulers = self.schedulers(active=False)
        result = check_schedulers(now, schedulers)
        assert not result
