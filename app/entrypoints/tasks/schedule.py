from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'update_sensors': {
        'task': 'update_sensors',
        'schedule': timedelta(seconds=30)
    },
    'update_current_power': {
        'task': 'update_current_power',
        'schedule': timedelta(seconds=10)
    },
    'invoke_mode': {
        'task': 'invoke_mode',
        'schedule': timedelta(minutes=10)
    },
    'notifications': {
        'task': 'notifications',
        'schedule': timedelta(minutes=5)
    },
    'update_smart_device_status': {
        'task': 'update_smart_device_status',
        'schedule': timedelta(minutes=6)
    },
}
