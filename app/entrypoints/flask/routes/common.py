import inject
from flask import Blueprint, Response, jsonify, request

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
    
    @common.route("/set_operation_mode")
    def set_operation_mode() -> Response:
        operation = request.args.get('operation')
        result = manage_op.set_active_operation_mode(operation)
        return jsonify(result)
    
    @common.route("/set_checking_low_cost")
    def set_checking_low_cost() -> Response:
        operation = request.args.get('operation')
        should_check = request.args.get('value')
        result = manage_op.set_checking_low_cost(operation, should_check)
        return jsonify(result)

    return common
