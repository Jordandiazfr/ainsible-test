from flask import Flask, jsonify
import os
from dbserver import PostGreSQL
import random
app = Flask(__name__)

r = random.randint(1, 9)
db = PostGreSQL()

db.create_table("jojo")
data = "Test" + str(r)
#db.insert("jojo", data)


@app.route("/")
def index():
    return "hello world"


@app.route("/db")
def showdb():
    result = db.select("jojo")
    return jsonify(result)


@app.route("/<env_var>")
def check_var(env_var):
    if env_var in os.environ:
        return(f'{env_var} value is {os.environ[env_var]}')
    else:
        return(f'{env_var} does not exist')


@app.route("/health")
def health():
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
