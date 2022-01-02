from tinytuya import OutletDevice

import logger
from app.domain.devices import Device, Status
from app.domain.interfaces import abstract_device_api

log = logger.get_logger("TuyaAPI")


class TuyaAPI(abstract_device_api):

    def set_status(self, device: Device, status: Status):
        tuya_device = OutletDevice(
            dev_id=device.device_id,
            address=device.ip_address,
            local_key=device.local_key
        )
        tuya_device.set_version(device.version)
        tuya_status = tuya_device.status()
        if tuya_status.get('Error'):
            log.error("Can't get tuya status: %s", tuya_status)
            return

        switch_status = tuya_status['dps']['1']
        if switch_status == status.value:
            log.info("Device: %s is already %s (switch_status: %s). Pass.", device.name, status.name, switch_status)
            return

        response = tuya_device.set_status(bool(status.value))
        log.info("Status successfully changed. Response: %s", response)
