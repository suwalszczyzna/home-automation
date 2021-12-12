from app import logger
from app.adapters.tuya import TuyaACL
from app.model.devices import BasicDevice

log = logger.get_logger("DeviceEvent")


class DeviceEvents:

    def __init__(self):
        self.tyua = TuyaACL()

    def turn_on(self, device: BasicDevice):
        log.info("Device %s: turn ON", device.name)
        self.tyua.turn_on(device.name)

    def turn_off(self, device: BasicDevice):
        log.info("Device %s: turn OFF", device.name)
        self.tyua.turn_off(device.name)
