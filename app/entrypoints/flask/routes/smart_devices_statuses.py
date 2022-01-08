
import inject
from flask import Blueprint, Response, jsonify

from app.domain.actions.smart_device_statuses import SmartDevicesStatuses


@inject.autoparams()
def create_device_status_blueprint(statuses: SmartDevicesStatuses) -> Blueprint:
    stats = Blueprint('device-statuses', __name__)

    @stats.route('/smart_device_statuses')
    def run() -> Response:
        result = statuses.get_smart_devices_statuses()
        return jsonify(result)

    return stats
