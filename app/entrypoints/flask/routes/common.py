import inject
import json

from flask import Blueprint, Response, jsonify, request

from app.domain.actions.manage_operation_modes import ManageOperationModes
from app.domain.actions.get_sensors_value import GetSensorsValue
from app.domain.actions.send_notification import SendNotification
from app.domain.actions.hysteresis import HysteresisActions


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


@inject.autoparams()
def create_common_blueprint(
        temp_actions: GetSensorsValue,
        manage_op: ManageOperationModes,
        notify: SendNotification,
        hysteresis: HysteresisActions) -> Blueprint:

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
        should_check = str2bool(request.args.get('value'))
        result = manage_op.set_checking_low_cost(operation, should_check)
        return jsonify(result)

    @common.route("/notify")
    def send_notify() -> Response:
        notify.send_notification()
        return jsonify({"code": "OK"})

    @common.route("/hysteresis", methods=['GET'])
    def get_hysteresis():
        return jsonify(hysteresis.get_hysteresis())

    @common.route("hysteresis", methods=['POST'])
    def update_hysteresis():
        data = json.loads(request.data)
        return jsonify(hysteresis.update_hysteresis(data['status'], data['value']))

    return common

