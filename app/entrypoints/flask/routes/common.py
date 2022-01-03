import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.temperatures import Tempareratures


@inject.autoparams()
def create_common_blueprint(temp_actions: Tempareratures) -> Blueprint:
    common = Blueprint("common", __name__)

    @common.route("/temperature")
    def get_temperatures() -> Response:
        result = temp_actions.get_actual_temperatures()
        return jsonify(result)

    return common
