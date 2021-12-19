from abc import ABC, abstractmethod
from typing import List

from app.domain.devices import Device
from app.domain.operation_modes import TempConfig, Operation
from app.domain.schedulers import WaterHeatSchedule, LowerCostPower


class AbstractDatabase(ABC):

    @abstractmethod
    def get_temp(self) -> TempConfig:
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
    def get_device_by_name(self, name: str) -> Device:
        pass
