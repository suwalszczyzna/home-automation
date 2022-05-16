from datetime import time
from typing import List

from app.domain.devices import Device, Status, TempConfig, CurrentPower, Hysteresis
from app.domain.operation_modes import Operation
from app.domain.schedulers import LowerCostPower, WaterHeatSchedule, Weekday
from app.domain.interfaces.abstract_database import AbstractDatabase
from app.domain.sensors import TempSensor


class FakeDatabase(AbstractDatabase):
    def __init__(self, db_uri: str) -> None:
        self.db_uri = db_uri

    def set_current_power(self, device_name: str, value: float) -> None:
        pass

    def get_current_power(self, device_name: str) -> float:
        return 1500.2

    def save_temp(self, sensor: TempSensor):
        pass

    def get_checking_schedule_status(self, operation: Operation) -> bool:
        return True

    def set_active_operation_mode(self, operation: Operation) -> None:
        pass

    def set_low_cost_checking(self, operation: Operation, value: bool) -> None:
        pass

    def add_water_heater_schedule(self, schedule: WaterHeatSchedule) -> None:
        pass

    def add_low_cost_power_schedule(self, schedule: LowerCostPower) -> None:
        pass

    def add_device(self, device: Device):
        pass

    def set_device_status(self, device_name: str, status: Status):
        pass

    def get_device_status(self, device_name: str) -> bool:
        return True

    def get_temp(self) -> TempConfig:
        return TempConfig(
            max_water_temp=50,
            water_temp=30,
            co_temp=50
        )

    def get_water_heater_schedulers(self) -> List[WaterHeatSchedule]:
        return []

    def get_low_cost_power_schedulers(self) -> List[LowerCostPower]:
        return [LowerCostPower(
            start=time(22, 0),
            end=time(8, 0),
            weekdays=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY]
        )]

    def get_active_operation_mode(self) -> Operation:
        return Operation.AUTO_MODE

    def get_device_by_name(self, name: str) -> Device:
        return Device(
            name="valve",
            device_id="39209388",
            ip_address="192.168.0.0",
            local_key="d9839j98h",
            version="3.3"
        )

    def set_notifier_status(self, device_name: str, value: bool) -> None:
        pass

    def get_notifier_status(self, device_name: str) -> bool:
        return True

    def get_chats(self) -> List[str]:
        return ['some-test-chat-id']

    def set_hysteresis_status(self, status: Status) -> None:
        pass

    def set_hysteresis_value(self, value: int) -> None:
        pass

    def get_hysteresis(self) -> Hysteresis:
        return Hysteresis(Status.TURN_ON, 10)
