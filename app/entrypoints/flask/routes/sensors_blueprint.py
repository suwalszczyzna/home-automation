import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.update_sensors_value import UpdateSensorsValue


@inject.autoparams()
def create_sensors_blueprint(update_sensors: UpdateSensorsValue) -> Blueprint:
    sensors = Blueprint('sensors', __name__)

    @sensors.route('/update_sensors_values')
    def run() -> Response:
        update_sensors.update_temp()
        return jsonify({
            "code": "ok"
        })

    return sensors
