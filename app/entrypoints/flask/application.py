from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from celery import Celery

from app.entrypoints.flask.configuration import configure_application, configure_inject, configure_celery
from app.entrypoints.flask.routes.mode_blueprint import create_mode_blueprint
from app.entrypoints.flask.routes.sensors_blueprint import create_sensors_blueprint
from app.entrypoints.flask.routes.common import create_common_blueprint
from app.entrypoints.flask.routes.smart_devices_statuses import create_device_status_blueprint

celery = Celery()


def create_application() -> Flask:
    load_dotenv()
    application = Flask(__name__)
    CORS(application)

    configure_application(application)
    configure_inject(application)

    application.register_blueprint(create_mode_blueprint(), url_prefix='/api')
    application.register_blueprint(create_sensors_blueprint(), url_prefix='/api')
    application.register_blueprint(create_common_blueprint(), url_prefix='/api')
    application.register_blueprint(create_device_status_blueprint(), url_prefix='/api')

    return application


def init_celery(application: Flask = None):
    application = application or create_application()
    celery.conf.update({
        "broker_url": application.config['CELERY_BROKER_URL'],
        "result_backend": application.config['CELERY_RESULT_BACKEND']
    })

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with application.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


if __name__ == '__main__':
    app = create_application()
    app.run(debug=True)
