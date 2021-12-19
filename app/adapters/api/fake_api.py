import logger
from app.domain.abstract_device_api import AbstractDeviceAPI
from app.domain.devices import Device, Status

log = logger.get_logger("DeviceEvent")


class FakeAPI(AbstractDeviceAPI):
    def set_status(self, device: Device, status: Status):
        log.info("Device %s, status: %s", device.name, status.name)
