import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.save_tempsensors_values import SaveTempsensorsValues


@inject.autoparams()
def create_sensors_blueprint(save_sensors: SaveTempsensorsValues) -> Blueprint:
    mode_blueprint = Blueprint('sensors', __name__)

    @mode_blueprint.route('/update_sensors_values')
    def run() -> Response:
        save_sensors.run()
        return jsonify({
            "code": "ok"
        })

    return mode_blueprint
