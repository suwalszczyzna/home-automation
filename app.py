from flask import Flask
from dotenv import load_dotenv

from configuration import configure_application, configure_inject
from app.entrypoints.mode_blueprint import create_mode_blueprint


def create_application() -> Flask:
    load_dotenv()
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(create_mode_blueprint(), url_prefix='/api')

    return application


if __name__ == '__main__':
    app = create_application()
    app.run(debug=True)
