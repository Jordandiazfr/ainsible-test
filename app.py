from flask import Flask, jsonify
import os
app = Flask(__name__)

a = os.environ.get('jojo')


@app.route("/")
def hello():
    return ("Hello world")


@app.route("/health")
def health():
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
