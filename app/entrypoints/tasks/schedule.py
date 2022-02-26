from datetime import timedelta

from ..flask.application import celery

CELERYBEAT_SCHEDULE = {
    'update_sensors': {
        'task': 'update_sensors',
        'schedule': timedelta(seconds=15)
    },
    'update_current_power': {
        'task': 'update_current_power',
        'schedule': timedelta(seconds=10)
    },
    'invoke_mode': {
        'task': 'invoke_mode',
        'schedule': timedelta(minutes=10)
    },
}
