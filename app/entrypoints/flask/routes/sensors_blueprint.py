import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.update_sensors_value import UpdateSensorsValue


@inject.autoparams()
def create_sensors_blueprint(update_sensors: UpdateSensorsValue) -> Blueprint:
    sensors = Blueprint('sensors', __name__)

    @sensors.route('/update_sensors_values')
    def update_sensors_values() -> Response:
        update_sensors.update_temp()
        return jsonify({
            "code": "ok"
        })

    @sensors.route('/update_current_power')
    def update_current_power() -> Response:
        update_sensors.update_current_power()
        return jsonify({
            "code": "ok"
        })

    return sensors
