from abc import ABC, abstractmethod
from typing import List

from app.domain.devices import Device, Status, TempConfig, CurrentPower
from app.domain.operation_modes import Operation
from app.domain.schedulers import WaterHeatSchedule, LowerCostPower
from app.domain.sensors import TempSensor


class AbstractDatabase(ABC):

    @abstractmethod
    def get_temp(self) -> TempConfig:
        pass

    @abstractmethod
    def save_temp(self, sensor: TempSensor):
        pass

    @abstractmethod
    def get_checking_schedule_status(self, operation: Operation) -> bool:
        pass

    @abstractmethod
    def get_water_heater_schedulers(self) -> List[WaterHeatSchedule]:
        pass

    @abstractmethod
    def get_low_cost_power_schedulers(self) -> List[LowerCostPower]:
        pass

    @abstractmethod
    def get_active_operation_mode(self) -> Operation:
        pass

    @abstractmethod
    def set_active_operation_mode(self, operation: Operation) -> None:
        pass
    
    @abstractmethod
    def set_low_cost_checking(self, operation: Operation, value: bool) -> None:
        pass

    @abstractmethod
    def get_device_by_name(self, name: str) -> Device:
        pass

    @abstractmethod
    def add_water_heater_schedule(self, schedule: WaterHeatSchedule) -> None:
        pass

    @abstractmethod
    def add_low_cost_power_schedule(self, schedule: LowerCostPower) -> None:
        pass

    @abstractmethod
    def add_device(self, device: Device):
        pass

    @abstractmethod
    def set_device_status(self, device_name: str, status: Status):
        pass

    @abstractmethod
    def get_device_status(self, device_name: str) -> bool:
        pass

    @abstractmethod
    def get_current_power(self, device_name: str) -> float:
        pass

    @abstractmethod
    def set_current_power(self, device_name: str, value: float) -> None:
        pass

    @abstractmethod
    def set_notifier_status(self, device_name: str, value: bool) -> None:
        pass

    @abstractmethod
    def get_notifier_status(self, device_name:str) -> bool:
        pass

    @abstractmethod
    def get_chats(self) -> List[int]:
        pass
