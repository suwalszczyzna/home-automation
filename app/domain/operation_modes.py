import abc
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

import inject

from app.domain.devices import Devices
from app.domain.schedulers import LowerCostPower, check_schedulers
from app.domain.actions.change_device_status import DeviceStatus


@dataclass
class TempConfig:
    max_water_temp: float
    water_temp: float
    co_temp: float


class Operation(Enum):
    AUTO_MODE = "auto_mode"
    AUTO_MODE_HEATER = "auto_mode_heater"


class OperationMode(abc.ABC):
    @abc.abstractmethod
    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):
        raise NotImplementedError


class AutoMode(OperationMode):
    @inject.autoparams('device_status')
    def __init__(self, device_status: DeviceStatus, lower_cost_power_schedulers: List[LowerCostPower]):
        self.schedules = lower_cost_power_schedulers
        self._device_status = device_status

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):

        if temp_config.water_temp > temp_config.max_water_temp:
            self._device_status.turn_off(Devices.COIL_VALVE.value)
            self._device_status.turn_off(Devices.WATER_HEATER.value)
        else:
            if temp_config.water_temp < temp_config.co_temp:
                self._device_status.turn_on(Devices.COIL_VALVE.value)
                self._device_status.turn_off(Devices.WATER_HEATER.value)
            elif temp_config.water_temp >= temp_config.co_temp:
                self._device_status.turn_off(Devices.COIL_VALVE.value)
                self.heater_turn_on(check_schedule)

    def heater_turn_on(self, check_schedule: bool):
        is_lower_cost = check_schedulers(datetime.now(), self.schedules)
        if not check_schedule:
            self._device_status.turn_on(Devices.WATER_HEATER.value)
        elif check_schedule and is_lower_cost:
            self._device_status.turn_on(Devices.WATER_HEATER.value)
        else:
            self._device_status.turn_off(Devices.WATER_HEATER.value)


class AutoModeHeaterPriority(OperationMode):
    @inject.autoparams()
    def __init__(self, device_status: DeviceStatus):
        self._device_status = device_status

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):
        if temp_config.water_temp < temp_config.max_water_temp:
            self._device_status.turn_off(Devices.COIL_VALVE.value)
            self._device_status.turn_on(Devices.WATER_HEATER.value)
        elif temp_config.water_temp >= temp_config.max_water_temp:
            self._device_status.turn_off(Devices.COIL_VALVE.value)
            self._device_status.turn_off(Devices.WATER_HEATER.value)
