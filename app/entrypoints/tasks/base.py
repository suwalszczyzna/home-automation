import inject

from ..flask.application import celery
from app.domain.actions.invoke_operation_mode import InvokeOperationMode
from app.domain.actions.update_sensors_value import UpdateSensorsValue
from app.domain.actions.send_notification import SendNotification


@celery.task(name='update_sensors')
@inject.autoparams()
def update_sensors(update_sensors: UpdateSensorsValue):
    update_sensors.update_temp()


@celery.task(name='update_current_power')
@inject.autoparams()
def update_current_power(update_sensors: UpdateSensorsValue):
    update_sensors.update_current_power()


@celery.task(name='invoke_mode')
@inject.autoparams()
def invoke_mode(invoke_operation_mode: InvokeOperationMode):
    invoke_operation_mode.execute()


@celery.task(name='notifications')
@inject.autoparams()
def send_notification(notifier: SendNotification):
    notifier.send_notification()

