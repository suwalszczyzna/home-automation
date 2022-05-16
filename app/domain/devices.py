from dataclasses import dataclass
from enum import Enum


class Devices(Enum):
    WATER_HEATER = "water_heater"
    COIL_VALVE = "valve"
    WASHER = "washer"
    DRYER = "dryer"


POWER_DEVICES = [Devices.WASHER.value, Devices.DRYER.value]


class Status(Enum):
    TURN_ON = 1
    TURN_OFF = 0


@dataclass
class NewDeviceStatus:
    device: Devices
    status: Status


@dataclass(frozen=True)
class Device:
    name: str
    device_id: str
    ip_address: str
    local_key: str
    version: str


@dataclass
class TempConfig:
    max_water_temp: float
    water_temp: float
    co_temp: float

    def to_dict(self):
        return {
            'max_water_temp': self.max_water_temp,
            'water_temp': self.water_temp,
            'co_temp': self.co_temp
        }


@dataclass
class CurrentPower:
    washer: float

    def to_dict(self):
        return {
            'washer': self.washer
        }


@dataclass
class Hysteresis:
    status: Status
    value: int

    def to_dict(self):
        return {
            "value": self.value,
            "status": bool(self.status.value)
        }

    @property
    def abs_value(self) -> int:
        if self.status == Status.TURN_OFF:
            return 0
        else:
            return self.value
