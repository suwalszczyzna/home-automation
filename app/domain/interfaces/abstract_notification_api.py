from abc import ABC
from typing import List


class AbstractNotificationApi(ABC):

    def send_notification(self, message: str, chat_ids: List):
        pass
