from datetime import time, datetime
from unittest import mock
from unittest.mock import call
from freezegun import freeze_time
from app.model.devices import Devices
from app.model.operation_modes import AutoMode, TempConfig, AutoModeHeaterPriority
from app.model.schedulers import LowerCostPower, Weekday

MAX_WATER_TEMP = 50.0


def auto_mode():
    schedule = LowerCostPower(
        start=time(8, 0),
        end=time(10, 0),
        weekdays=[Weekday.MONDAY, Weekday.TUESDAY]
    )
    return AutoMode(schedule)


auto_mode = auto_mode()


@freeze_time(datetime(2021, 12, 12, 16, 31))  # SUNDAY
@mock.patch("app.adapters.device_events.turn_off")
@mock.patch("app.adapters.device_events.turn_on")
class TestAutoModeWithoutAdditionalScheduleChecking:

    def test_when_water_temp_is_gt_co_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        turn_off.assert_called_with(Devices.COIL_VALVE)
        turn_on.assert_called_with(Devices.WATER_HEATER)

    def test_when_water_temp_is_eq_co_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=40.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        turn_off.assert_called_with(Devices.COIL_VALVE)
        turn_on.assert_called_with(Devices.WATER_HEATER)

    def test_when_co_temp_is_gt_water_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=30.0,
            co_temp=50.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        turn_off.assert_called_with(Devices.WATER_HEATER)
        turn_on.assert_called_with(Devices.COIL_VALVE)

    def test_when_water_temp_is_gt_co_temp_and_max_water_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=55.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )

        auto_mode.invoke(temp_config)

        turn_off.assert_has_calls([call(Devices.COIL_VALVE), call(Devices.WATER_HEATER)])


@freeze_time(datetime(2021, 12, 12, 16, 31))  # SUNDAY
@mock.patch("app.adapters.device_events.turn_off")
@mock.patch("app.adapters.device_events.turn_on")
class TestAutoModeWithAdditionalScheduleChecking:
    temp_config = TempConfig(
        water_temp=40.0,
        co_temp=30.0,
        max_water_temp=MAX_WATER_TEMP
    )

    def test_when_water_temp_is_gt_co_temp_and_not_in_schedule(self, turn_on, turn_off):
        schedule = LowerCostPower(
            start=time(10, 0),
            end=time(11, 0),
            weekdays=[Weekday.SATURDAY, Weekday.SUNDAY]
        )

        auto_mode_op = AutoMode(schedule)
        auto_mode_op.invoke(self.temp_config, check_schedule=True)

        turn_off.assert_has_calls([call(Devices.COIL_VALVE), call(Devices.WATER_HEATER)])

    def test_when_water_temp_is_gt_co_temp_and_in_schedule(self, turn_on, turn_off):
        schedule = LowerCostPower(
            start=time(10, 0),
            end=time(18, 0),
            weekdays=[Weekday.SATURDAY, Weekday.SUNDAY]
        )

        auto_mode_op = AutoMode(schedule)
        auto_mode_op.invoke(self.temp_config, check_schedule=True)

        turn_off.assert_called_with(Devices.COIL_VALVE)
        turn_on.assert_called_with(Devices.WATER_HEATER)


@mock.patch("app.adapters.device_events.turn_off")
@mock.patch("app.adapters.device_events.turn_on")
class TestAutoModeHeaterPriority:

    def test_when_water_temp_is_lt_max_water_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=40.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )
        heater_priority = AutoModeHeaterPriority()
        heater_priority.invoke(temp_config)

        turn_off.assert_called_with(Devices.COIL_VALVE)
        turn_on.assert_called_with(Devices.WATER_HEATER)

    def test_when_water_temp_is_gt_max_water_temp(self, turn_on, turn_off):
        temp_config = TempConfig(
            water_temp=60.0,
            co_temp=30.0,
            max_water_temp=MAX_WATER_TEMP
        )
        heater_priority = AutoModeHeaterPriority()
        heater_priority.invoke(temp_config)

        turn_off.assert_has_calls([call(Devices.COIL_VALVE), call(Devices.WATER_HEATER)])
