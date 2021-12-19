from app import logger
from app.adapters.tuya import TuyaACL
from app.domain.devices import Devices

log = logger.get_logger("DeviceEvent")

tyua = TuyaACL()


def turn_on(device_enum: Devices):
    log.info("Device %s: turn ON", device_enum.value)
    tyua.turn_on(device_enum.value)


def turn_off(device_enum: Devices):
    log.info("Device %s: turn OFF", device_enum.value)
    tyua.turn_off(device_enum.value)
