from datetime import time
from freezegun import freeze_time
from app.model.schedulers import LowerCostPowerSchedule, Weekday, Schedule


class TestScheduleBaseClass:
    def test_in_weekday(self):
        weekday = 1  # TUE
        schedule = Schedule(
            start=time(0, 0),
            end=time(1, 0),
            weekdays=[Weekday.MONDAY, Weekday.FRIDAY]
        )

        assert not schedule.in_weekdays(weekday)


@freeze_time("2021-12-11 10:00")  # saturday
class TestLowerCostPowerSchedule:

    def test_is_low_cost_without_weekdays(self):
        schedule = LowerCostPowerSchedule(
            start=time(7, 0),
            end=time(16, 0),
            weekdays=[]
        )
        assert schedule.is_low_cost()

        schedule_2 = LowerCostPowerSchedule(
            start=time(7, 0),
            end=time(9, 0),
            weekdays=[]
        )
        assert not schedule_2.is_low_cost()

    def test_is_low_cost_with_weekdays(self):
        schedule = LowerCostPowerSchedule(
            start=time(7, 0),
            end=time(16, 0),
            weekdays=[Weekday.MONDAY, Weekday.SUNDAY, Weekday.SATURDAY]
        )

        assert schedule.is_low_cost()
