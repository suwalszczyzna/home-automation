import os
from time import sleep

import requests
from dotenv import load_dotenv

import logger

log = logger.get_logger("invoke-operation-mode")


def run_invoke_operation_mode():
    try:
        requests.get("http://127.0.0.1:5000/api/invoke", timeout=5)
    except Exception as e:
        log.error("Error", exc_info=e)


if __name__ == '__main__':
    load_dotenv()
    while True:
        run_invoke_operation_mode()
        sleep(int(os.getenv('INVOKE_OPERATION_MODE', default='60')))
