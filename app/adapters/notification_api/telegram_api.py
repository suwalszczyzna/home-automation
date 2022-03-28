from typing import List

import logger
import telegram
from app.domain.interfaces.abstract_notification_api import AbstractNotificationApi

log = logger.get_logger("TelegramAPI")


class TelegramAPI(AbstractNotificationApi):
    def __init__(self, token):
        self.bot = telegram.Bot(token=token)

    def send_notification(self, message: str, chats: List[int]):
        for chat_id in chats:
            log.info("Sending notification to chat id: %s", chat_id)
            try:
                self.bot.send_message(text=message, chat_id=chat_id)
            except Exception as e:
                log.error("Somethings goes wrong during send notification, chat id: %s", chat_id)
