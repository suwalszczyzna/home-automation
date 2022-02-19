import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.manage_operation_modes import ManageOperationModes
from app.domain.actions.temperatures import Tempareratures


@inject.autoparams()
def create_common_blueprint(temp_actions: Tempareratures, manage_op: ManageOperationModes) -> Blueprint:
    common = Blueprint("common", __name__)

    @common.route("/temperature")
    def get_temperatures() -> Response:
        result = temp_actions.get_actual_temperatures()
        return jsonify(result)

    @common.route("/get_actual_mode")
    def get_actual_mode() -> Response:
        result = manage_op.get_active_operation_mode()
        return jsonify(result)

    return common
