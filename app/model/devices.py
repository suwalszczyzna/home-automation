from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class BasicDevice:
    name: Optional[str] = ""
    is_on: bool = False

    def update_status(self, status: bool):
        self.is_on = status


class CoilValve(BasicDevice):
    pass


class WaterHeater(BasicDevice):
    pass


@dataclass
class Sensor:
    value: Optional[float] = 0

    def set_value(self, value: float):
        self.value = value


class WaterTemp(Sensor):
    pass


class COTemp(Sensor):
    pass


class Devices(Enum):
    WATER_HEATER = "water_heater"
    COIL_VALVE = "coil_valve"
