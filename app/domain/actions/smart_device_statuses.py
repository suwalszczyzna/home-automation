import inject

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.devices import Devices


class SmartDevicesStatuses:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    def get_smart_devices_statuses(self):
        return {
            "heater": self._db.get_device_status(Devices.WATER_HEATER.value),
            "valve": self._db.get_device_status(Devices.COIL_VALVE.value)
        }
