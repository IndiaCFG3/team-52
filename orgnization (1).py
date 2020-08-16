from flask import request, session
from flask import jsonify
from db_config import mysql
import re


@app.route('/api/organization/createuser', methods=['POST'])
def index():
    if request.method == "POST":
        username = request.args.get('UserName')
        password = request.args.get('Password')
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO organization(org_name, org_password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        response = 'successfully cread user in organization'
        return jsonify(response)


@app.route('/api/organization/login', methods=['POST'])
def login():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cur = mysql.connect().cursor()
    cur.execute("SELECT * from organization where Username='" +
                username + "' and Password='" + password + "'")
    data = cur.fetchone()
    if data is None:
        response = False
        response.status_code = 401
        return jsonify(response)  # "Username or Password is wrong"
    else:
        response = True
        response.status_code = 200
        return jsonify(response)  # "Logged in successfully"

# extra route to get all the data
@app.route('/api/organization/getalldata', methods=['GET'])
def getalldata():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * from organization")
    data = cur.fetchall()
    cur.close()
    if data is None:
        response = data
        response.status_code = 204
        return jsonify(response)
    else:
        response = data
        response.status_code = 200
        return jsonify(response)
