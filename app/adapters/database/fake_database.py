from datetime import time
from typing import List

from app.domain.abstract_database import AbstractDatabase
from app.domain.operation_modes import Operation, TempConfig
from app.domain.schedulers import LowerCostPower, WaterHeatSchedule, Weekday


class FakeDatabase(AbstractDatabase):
    def __init__(self, db_uri: str) -> None:
        self.db_uri = db_uri

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
