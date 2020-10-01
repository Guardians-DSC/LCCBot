from flask import Flask
from flask import jsonify
from api.services.scheduleService import *

@app.route('/schedule')
def schedule():
    schedules = scheduleService()
    return jsonify(schedule)