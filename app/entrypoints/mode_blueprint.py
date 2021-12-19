import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.invoke_operation_mode import InvokeOperationMode


@inject.autoparams()
def create_mode_blueprint(invoke_operation_mode: InvokeOperationMode) -> Blueprint:
    mode_blueprint = Blueprint('mode', __name__)

    @mode_blueprint.route('/invoke')
    def invoke_mode() -> Response:
        invoke_operation_mode.execute()
        return jsonify({
            "code": "ok"
        })

    return mode_blueprint
