from datetime import datetime
from enum import Enum
from typing import List

from app.domain.devices import Devices, Status, NewDeviceStatus, TempConfig
from app.domain.schedulers import LowerCostPower, check_schedulers


class Operation(Enum):
    AUTO_MODE = "auto_mode"
    AUTO_MODE_HEATER = "auto_mode_heater"


def new_statuses(new_valve_status: Status, new_water_heater_status: Status) -> List[NewDeviceStatus]:
    return [
        NewDeviceStatus(Devices.COIL_VALVE, new_valve_status),
        NewDeviceStatus(Devices.WATER_HEATER, new_water_heater_status),
    ]


hysteresis = 10


class OperationMode:
    def __init__(self, lower_cost_power_schedulers: List[LowerCostPower]):
        self.schedules = lower_cost_power_schedulers

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False) -> List[NewDeviceStatus]:
        raise NotImplementedError

    def heater_turn_on(self, check_schedule: bool) -> Status:
        is_lower_cost = check_schedulers(datetime.now(), self.schedules)

        if (not check_schedule) or (check_schedule and is_lower_cost):
            return Status.TURN_ON

        return Status.TURN_OFF


class AutoMode(OperationMode):
    def __init__(self, lower_cost_power_schedulers: List[LowerCostPower]):
        super().__init__(lower_cost_power_schedulers)

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False) -> List[NewDeviceStatus]:

        if temp_config.water_temp > temp_config.max_water_temp:
            return new_statuses(
                new_valve_status=Status.TURN_OFF,
                new_water_heater_status=Status.TURN_OFF
            )

        else:
            if self.valve_should_turn_on(temp_config):
                return new_statuses(
                    new_valve_status=Status.TURN_ON,
                    new_water_heater_status=Status.TURN_OFF
                )

            elif temp_config.water_temp < (temp_config.max_water_temp - hysteresis):
                return new_statuses(
                    new_valve_status=Status.TURN_OFF,
                    new_water_heater_status=self.heater_turn_on(check_schedule)
                )

        return new_statuses(
            new_valve_status=Status.TURN_OFF,
            new_water_heater_status=Status.TURN_OFF
        )

    def temp_diff_water_vs_co(self, temp_config: TempConfig) -> float:
        return temp_config.co_temp - temp_config.water_temp

    def valve_should_turn_on(self, temp_config: TempConfig) -> bool:
        co_gt_water = temp_config.water_temp < temp_config.co_temp
        co_gt_min = 40 < temp_config.co_temp

        return co_gt_min and co_gt_water and self.temp_diff_water_vs_co(temp_config) >= 5


class AutoModeHeaterPriority(OperationMode):

    def __init__(self, lower_cost_power_schedulers: List[LowerCostPower]):
        super().__init__(lower_cost_power_schedulers)

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False) -> List[NewDeviceStatus]:
        if temp_config.water_temp < (temp_config.max_water_temp - hysteresis):
            return new_statuses(
                new_valve_status=Status.TURN_OFF,
                new_water_heater_status=self.heater_turn_on(check_schedule)
            )

        elif temp_config.water_temp >= temp_config.max_water_temp:
            return new_statuses(
                new_valve_status=Status.TURN_OFF,
                new_water_heater_status=Status.TURN_OFF
            )
