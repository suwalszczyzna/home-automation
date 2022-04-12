from pprint import pprint

from tinytuya import OutletDevice

import logger
from app.domain.devices import Device, Status
from app.domain.interfaces.abstract_device_api import AbstractDeviceAPI

log = logger.get_logger("TuyaAPI")


class TuyaAPI(AbstractDeviceAPI):

    @staticmethod
    def create_tuya_device(device):
        tuya_device = OutletDevice(
            dev_id=device.device_id,
            address=device.ip_address,
            local_key=device.local_key
        )
        tuya_device.set_socketTimeout(3)
        tuya_device.set_version(device.version)
        return tuya_device

    def get_device_switch_status(self, tuya_device: OutletDevice):
        tuya_status = tuya_device.status()
        if tuya_status.get('Error'):
            log.info("Can't get tuya status: %s", tuya_status)
            return False
        log.info(pprint(tuya_status))
        return tuya_status['dps']['1']

    def set_switch_status(self, device: Device, status: Status) -> bool:
        log.info("Changing status for device: %s", device.name)
        try:
            tuya_device = self.create_tuya_device(device)

            if bool(status.value):
                tuya_device.turn_on()
            else:
                tuya_device.turn_off()
            log.info("Send signal to %s device: %s", "turn_on" if bool(status.value) else "turn_off", device.name)
            return True
        except Exception as e:
            log.error("Problem with TuyaAPI device %s", device.name, exc_info=e)
            return False

    def get_current_power(self, device: Device) -> float:
        try:
            tuya_device = self.create_tuya_device(device)
            tuya_status = tuya_device.status()
            if tuya_status.get('Error'):
                log.info("Can't get current power: %s", tuya_status)
                return 0.0

            power_dps = '19'
            power = tuya_status['dps'].get(power_dps, 0) / 10
            log.info(f'Current power of {device.name}: {power} W')
            return power
        except Exception as e:
            log.error("Problem with TuyaAPI with device %s", device.name, exc_info=e)
            return 0.0
