from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return 'Bonjour, je suis arrivé ici depuis ainsible, jaime pas cette fille'


@app.route("/health")
def health():
    return jsonify({'status': 'ok'})


# if __name__ == "__main__":
#   app.run(host='0.0.0.0', debug=True, port=5000)
#
