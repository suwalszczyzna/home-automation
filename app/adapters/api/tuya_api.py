from tinytuya import OutletDevice

import logger
from app.domain.devices import Device, Status
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI

log = logger.get_logger("TuyaAPI")


class TuyaAPI(AbstractDeviceAPI):

    def set_status(self, device: Device, status: Status) -> bool:
        log.info("Chaning status for dev: %s", device.name)
        try:
            tuya_device = OutletDevice(
                dev_id=device.device_id,
                address=device.ip_address,
                local_key=device.local_key
            )
            tuya_device.set_socketTimeout(3)
            tuya_device.set_version(device.version)
            tuya_status = tuya_device.status()
            if tuya_status.get('Error'):
                log.info("Can't get tuya status: %s", tuya_status)
                return False

            switch_status = tuya_status['dps']['1']
            if switch_status == status.value:
                log.info("Device: %s is already %s (switch_status: %s). Pass.", device.name, status.name, switch_status)
                return True

            response = tuya_device.set_status(bool(status.value))
            log.info("Device: %s status successfully changed. Response: %s", device.name, response)
            return True
        except Exception as e:
            log.error("Problem with TuyaAPI with device %s", device.name, exc_info=e)
            return False
