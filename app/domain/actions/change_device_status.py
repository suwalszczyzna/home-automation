from typing import List

import inject

from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.devices import NewDeviceStatus


class ChangeDeviceStatus:
    @inject.autoparams()
    def __init__(self, api: AbstractDeviceAPI, db: AbstractDatabase):
        self._api = api
        self._db = db

    def run(self, new_device_statuses: List[NewDeviceStatus]):
        for status in new_device_statuses:
            device = self._db.get_device_by_name(status.device.value)
            self._api.set_status(device, status.status)
