import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.temperatures import Temperatures


@inject.autoparams()
def create_common_blueprint(temp_actions: Temperatures) -> Blueprint:
    common = Blueprint("common", __name__)

    @common.route("/temperature")
    def get_temperatures() -> Response:
        result = temp_actions.get_actual_temperatures()
        return jsonify(result)

    @common.route("/clean-temp-history")
    def clean_temp_history() -> Response:
        return jsonify(temp_actions.clean_temp_history())

    return common
