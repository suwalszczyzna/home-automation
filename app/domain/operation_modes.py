import abc
from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.adapters import device_events
from app.domain.devices import Devices
from app.domain.schedulers import LowerCostPower, check_schedulers


@dataclass
class TempConfig:
    max_water_temp: float
    water_temp: float
    co_temp: float


class OperationMode(abc.ABC):
    @abc.abstractmethod
    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):
        raise NotImplementedError


class AutoMode(OperationMode):
    def __init__(self, lower_cost_power_schedulers: List[LowerCostPower]):
        self.schedules = lower_cost_power_schedulers

    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):

        if temp_config.water_temp > temp_config.max_water_temp:
            device_events.turn_off(Devices.COIL_VALVE)
            device_events.turn_off(Devices.WATER_HEATER)
        else:
            if temp_config.water_temp < temp_config.co_temp:
                device_events.turn_on(Devices.COIL_VALVE)
                device_events.turn_off(Devices.WATER_HEATER)
            elif temp_config.water_temp >= temp_config.co_temp:
                device_events.turn_off(Devices.COIL_VALVE)
                self.heater_turn_on(check_schedule)

    def heater_turn_on(self, check_schedule: bool):
        is_lower_cost = check_schedulers(datetime.now(), self.schedules)
        if not check_schedule:
            device_events.turn_on(Devices.WATER_HEATER)
        elif check_schedule and is_lower_cost:
            device_events.turn_on(Devices.WATER_HEATER)
        else:
            device_events.turn_off(Devices.WATER_HEATER)


class AutoModeHeaterPriority(OperationMode):
    def invoke(self, temp_config: TempConfig, check_schedule: bool = False):
        if temp_config.water_temp < temp_config.max_water_temp:
            device_events.turn_off(Devices.COIL_VALVE)
            device_events.turn_on(Devices.WATER_HEATER)
        elif temp_config.water_temp >= temp_config.max_water_temp:
            device_events.turn_off(Devices.COIL_VALVE)
            device_events.turn_off(Devices.WATER_HEATER)
