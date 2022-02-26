from app.entrypoints.flask.application import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("app.tasks.base",)
