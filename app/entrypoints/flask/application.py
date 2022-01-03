from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from app.entrypoints.flask.configuration import configure_application, configure_inject
from app.entrypoints.flask.routes.mode_blueprint import create_mode_blueprint
from app.entrypoints.flask.routes.sensors_blueprint import create_sensors_blueprint
from app.entrypoints.flask.routes.common import create_common_blueprint


def create_application() -> Flask:
    load_dotenv()
    application = Flask(__name__)
    CORS(application)

    configure_application(application)
    configure_inject(application)

    application.register_blueprint(create_mode_blueprint(), url_prefix='/api')
    application.register_blueprint(create_sensors_blueprint(), url_prefix='/api')
    application.register_blueprint(create_common_blueprint(), url_prefix='/api')

    return application


if __name__ == '__main__':
    app = create_application()
    app.run(debug=True)
