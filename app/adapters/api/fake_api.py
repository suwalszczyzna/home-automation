import logger
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI
from app.domain.devices import Device, Status

log = logger.get_logger("DeviceEvent")


class FakeAPI(AbstractDeviceAPI):
    def set_status(self, device: Device, status: Status) -> bool:
        log.info("Device %s, status: %s", device.name, status.name)
        return True
