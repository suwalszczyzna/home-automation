from abc import ABC, abstractmethod
from typing import List

from app.domain.sensors import TempSensor


class AbstractSensorApi(ABC):

    @abstractmethod
    def get_all_sensors(self) -> List[TempSensor]:
        pass
