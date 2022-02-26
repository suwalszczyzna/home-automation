from abc import ABC, abstractmethod

from app.domain.devices import Device, Status


class AbstractDeviceAPI(ABC):
    @abstractmethod
    def set_switch_status(self, device: Device, status: Status) -> bool:
        pass

    @abstractmethod
    def get_current_power(self, device: Device) -> float:
        pass
