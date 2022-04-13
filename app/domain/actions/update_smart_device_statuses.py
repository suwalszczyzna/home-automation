import inject

import logger
from app.domain.devices import Devices
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI

log = logger.get_logger(__name__)


class UpdateSmartDeviceStatuses:
    @inject.autoparams()
    def __init__(self, _api: AbstractDeviceAPI, _db: AbstractDatabase):
        self._api = _api
        self._db = _db

    def run(self):
        log.info("Run update status from API")
        device = self._db.get_device_by_name(Devices.WATER_HEATER.value)
        status = self._api.get_device_switch_status(device)
        self._db.set_device_status(device.name, status)
