from flask import request, session
from flask import jsonify
from db_config import mysql
import re


@app.route('/api/school/createschool', methods=['POST'])
def createschool():
    if request.method == "POST":
        schoolname = request.args.get('schoolname')
        schoolpassword = request.args.get('schoolpassword')
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO school(school_name, school_password) VALUES (%s, %s)", (schoolname, schoolpassword))
        mysql.connection.commit()
        cur.close()
        response = 'successfully cread user in organization'
        response.status_code = 200
        return jsonify(response)


@app.route('/api/school/login', methods=['POST'])
def login():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from school where Username='" +
                   username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        response = False
        response.status_code = 401
        return jsonify(response)  # "Username or Password is wrong"
    else:
        response = True
        response.status_code = 200
        return jsonify(response)  # "Logged in successfully"


@app.route('/api/school/deleteschool', methods=['POST'])
def deleteschool():
    school_id = request.args.get('school_id')
    cursor = mysql.connect().cursor()
    cursor.execute("DELETE FROM school WHERE id = %s", (school_id))
    mysql.connection.commit()
    cursor.close()
    response = 'successfully deleted school'
    response.status_code = 200
    return jsonify(response)

# extra route to get all the data
@app.route('/api/school/getalldata', methods=['GET'])
def getalldata():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * from school")
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
