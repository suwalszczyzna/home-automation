import logger
import telegram
from app.domain.interfaces.abstract_notification_api import AbstractNotificationApi

log = logger.get_logger("TelegramAPI")


class TelegramAPI(AbstractNotificationApi):
    def __init__(self, token):
        self.bot = telegram.Bot(token=token)

    def send_notification(self, message: str):
        updates = self.bot.get_updates()

        for chat_id in set([update.message.chat.id for update in updates]):
            log.info("Sending notification to chat id: ", chat_id)
            try:
                self.bot.send_message(text=message, chat_id=chat_id)
            except Exception as e:
                log.error("Somethings goes wrong during send notification, chat id: ", chat_id)
