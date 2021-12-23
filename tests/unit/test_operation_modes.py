from datetime import time, datetime
from unittest import mock

from freezegun import freeze_time

from app.domain.devices import Status
from app.domain.operation_modes import AutoMode, TempConfig, AutoModeHeaterPriority
from app.domain.schedulers import LowerCostPower, Weekday

MAX_WATER_TEMP = 50.0


def auto_mode():
    schedule = LowerCostPower(
        start=time(8, 0),
        end=time(10, 0),
        weekdays=[Weekday.MONDAY, Weekday.TUESDAY]
    )
    return AutoMode([schedule])


auto_mode = auto_mode()


@freeze_time(datetime(2021, 12, 12, 16, 31))  # SUNDAY
@mock.patch("app.domain.operation_modes.new_statuses")
class TestAutoModeWithoutAdditionalScheduleChecking:

    def test_when_water_temp_is_gt_co_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_ON
        )

    def test_when_water_temp_is_eq_co_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=40.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_ON
        )

    def test_when_co_temp_is_gt_water_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=30.0,
            co_temp=50.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_ON,
            new_water_heater_status=Status.TURN_OFF
        )

    def test_when_water_temp_is_gt_co_temp_and_max_water_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=55.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_OFF
        )


@freeze_time(datetime(2021, 12, 12, 16, 31))  # SUNDAY
@mock.patch("app.domain.operation_modes.new_statuses")
class TestAutoModeWithAdditionalScheduleChecking:
    temp_config = TempConfig(
        water_temp=40.0,
        co_temp=30.0,
        max_water_temp=MAX_WATER_TEMP
    )

    def test_when_water_temp_is_gt_co_temp_and_not_in_schedule(self, new_statuses):
        schedule = LowerCostPower(
            start=time(10, 0),
            end=time(11, 0),
            weekdays=[Weekday.SATURDAY, Weekday.SUNDAY]
        )

        auto_mode_op = AutoMode([schedule])
        auto_mode_op.invoke(self.temp_config, check_schedule=True)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_OFF
        )

    def test_when_water_temp_is_gt_co_temp_and_in_schedule(self, new_statuses):
        schedule = LowerCostPower(
            start=time(10, 0),
            end=time(18, 0),
            weekdays=[Weekday.SATURDAY, Weekday.SUNDAY]
        )

        auto_mode_op = AutoMode([schedule])
        auto_mode_op.invoke(self.temp_config, check_schedule=True)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_ON
        )


@mock.patch("app.domain.operation_modes.new_statuses")
class TestAutoModeHeaterPriority:

    def test_when_water_temp_is_lt_max_water_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )
        heater_priority = AutoModeHeaterPriority()
        heater_priority.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_ON
        )

    def test_when_water_temp_is_gt_max_water_temp(self, new_statuses):
        temp_config = TempConfig(
            water_temp=60.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )
        heater_priority = AutoModeHeaterPriority()
        heater_priority.invoke(temp_config)

        new_statuses.assert_called_with(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_OFF
        )
