from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def status():
    return ''

if __name__ == "__main__":
    app.run()