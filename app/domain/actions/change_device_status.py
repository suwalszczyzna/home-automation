import inject

from app.domain.abstract_database import AbstractDatabase
from app.domain.abstract_device_api import AbstractDeviceAPI
from app.domain.devices import Status


class DeviceStatus:
    @inject.autoparams()
    def __init__(self, api: AbstractDeviceAPI, db: AbstractDatabase):
        self._api = api
        self._db = db

    def turn_off(self, device_name: str):
        device = self._db.get_device_by_name(device_name)
        self._api.set_status(device, Status.TURN_OFF)

    def turn_on(self, device_name: str):
        device = self._db.get_device_by_name(device_name)
        self._api.set_status(device, Status.TURN_ON)
