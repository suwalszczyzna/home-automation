from app.entrypoints.flask.application import init_celery
from app.entrypoints.tasks.schedule import CELERYBEAT_SCHEDULE

app = init_celery()
app.conf.imports = app.conf.imports + ("app.entrypoints.tasks.base",)
app.conf.beat_schedule = CELERYBEAT_SCHEDULE