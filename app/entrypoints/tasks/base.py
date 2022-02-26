from ..flask.application import celery


@celery.task(name='dummy')
def dummy_task():
    print("SOME DUMMY TASK")
