import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.save_tempsensors_values import SaveTempsensorsValues


@inject.autoparams()
def create_sensors_blueprint(save_sensors: SaveTempsensorsValues) -> Blueprint:
    sensors = Blueprint('sensors', __name__)

    @sensors.route('/update_sensors_values')
    def run() -> Response:
        save_sensors.run()
        return jsonify({
            "code": "ok"
        })

    return sensors
