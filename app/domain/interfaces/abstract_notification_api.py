from abc import ABC, abstractmethod
from typing import List

from app.domain.notification import Subscriber


class AbstractNotificationApi(ABC):

    def send_notification(self, receivers: List[Subscriber], message: str):
        pass
