from abc import ABC, abstractmethod

from app.domain.devices import Device, Status


class AbstractDeviceAPI(ABC):
    @abstractmethod
    def set_status(self, device: Device, status: Status):
        pass
