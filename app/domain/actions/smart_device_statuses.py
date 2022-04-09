import inject

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.devices import Devices


class SmartDevicesStatuses:
    @inject.autoparams()
    def __init__(self, db: AbstractDatabase):
        self._db = db

    @staticmethod
    def is_device_on(current_power: float) -> bool:
        if current_power > 1:
            return True
        return False

    def _washer_current_power(self):
        return self._db.get_current_power(Devices.WASHER.value)

    def _dryer_current_power(self):
        return self._db.get_current_power(Devices.DRYER.value)

    def get_smart_devices_statuses(self):
        return {
            "heater": self._db.get_device_status(Devices.WATER_HEATER.value),
            "valve": self._db.get_device_status(Devices.COIL_VALVE.value),
            "washer": {
                "power": self._washer_current_power(),
                "status": self.is_device_on(self._washer_current_power())
            },
            "dryer": {
                "power": self._dryer_current_power(),
                "status": self.is_device_on(self._dryer_current_power())
            }
        }

    def get_current_power(self):
        return {
            "washer": self._washer_current_power()
        }
