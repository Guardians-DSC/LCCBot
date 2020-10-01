from flask import Flask
from flask import jsonify

@app.route('/ping')
def status():
    return ''