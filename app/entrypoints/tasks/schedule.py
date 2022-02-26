from datetime import timedelta

from ..flask.application import celery

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'dummy',
        'schedule': timedelta(seconds=10)
    },
}
