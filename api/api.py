from flask import Flask
from flask import jsonify
from src.routes import ping_blueprint, scheduler_blueprint, status_blueprint

app = Flask(__name__)
app.register_blueprint(scheduler_blueprint)
app.register_blueprint(ping_blueprint)
app.register_blueprint(status_blueprint)

if __name__ == "__main__":
    app.run()