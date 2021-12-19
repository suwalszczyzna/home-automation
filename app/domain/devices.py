from dataclasses import dataclass
from enum import Enum


class Devices(Enum):
    WATER_HEATER = "water_heater"
    COIL_VALVE = "valve"


class Status(Enum):
    TURN_ON = 1
    TURN_OFF = 0


@dataclass(frozen=True)
class Device:
    name: str
    device_id: str
    ip_address: str
    local_key: str
