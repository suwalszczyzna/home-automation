from abc import ABC, abstractmethod

from tinytuya import OutletDevice

from app.domain.devices import Device, Status


class AbstractDeviceAPI(ABC):
    @abstractmethod
    def set_switch_status(self, device: Device, status: Status) -> bool:
        pass

    @abstractmethod
    def get_current_power(self, device: Device) -> float:
        pass

    @abstractmethod
    def get_device_switch_status(self, device: Device) -> Status:
        pass
