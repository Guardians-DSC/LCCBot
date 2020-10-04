from flask import Blueprint
from flask import jsonify
from ..services.scheduleService import scheduleService

scheduler_blueprint = Blueprint("scheduler", __name__)


@scheduler_blueprint.route("/schedule")
def scheduler():
    schedule = scheduleService()
    return jsonify(schedule)