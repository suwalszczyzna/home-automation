from datetime import time, datetime
from app.domain.schedulers import Weekday, Schedule


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
