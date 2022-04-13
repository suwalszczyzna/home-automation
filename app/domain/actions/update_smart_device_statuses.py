import inject
import logger

from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.devices import POWER_DEVICES, Device

log = logger.get_logger(__name__)


class UpdateSmartDeviceStatuses:
    @inject.autoparams()
    def __init__(self, _api: AbstractDeviceAPI, _db: AbstractDatabase):
        self._api = _api
        self._db = _db

    def run(self):
        log.info("Run update status from API")
        for device_name in POWER_DEVICES:
            device = self._db.get_device_by_name(device_name)
            status = self._api.get_device_switch_status(device)
            self._db.set_device_status(device.name, status)
