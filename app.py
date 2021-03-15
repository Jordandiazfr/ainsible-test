from flask import Flask, jsonify, render_template
import os
from dbserver import PostGreSQL
import random
app = Flask(__name__)

r = random.randint(1, 9)
db = PostGreSQL()

db.create_table("jojo")
data = "Test" + str(r)
db.insert("jojo", data)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/id')
def showData():
    myresult = db.exec(
        """SELECT id FROM jojo ORDER BY id DESC LIMIT 1""")
    return jsonify(myresult)


@app.route('/inc')
def addData():
    try:
        conn = psycopg2.connect(host='localhost',
                                user='test',
                                database='dbtest',
                                password='pw')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jojo (id) VALUES (DEFAULT);")
        conn.commit()
        return "Une valeur à été ajouté"
    except Exception as e:
        print("Error :", e)


@app.route("/<nroute>")
def route(nroute):
    return render_template("route.html", route=nroute)


@app.route("/db")
def showdb():
    result = db.select("jojo")
    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
