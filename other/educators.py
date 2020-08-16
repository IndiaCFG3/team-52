from flask import request, session
from flask import jsonify
from db_config import mysql
import re


@app.route('/api/educator/createeducator', methods=['POST'])
def createteacher():
    if request.method == "POST":
        teachername = request.args.get('teachername')
        teacherpassword = request.args.get('teacherpassword')
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO educator(teacher_name, teacher_password) VALUES (%s, %s)", (teachername, teacherpassword))
        mysql.connection.commit()
        cur.close()
        response = 'successfully cread user in organization'
        response.status_code = 200
        return jsonify(response)


@app.route('/api/educator/login', methods=['POST'])
def login():
    teachername = request.args.get('teachername')
    teacherpassword = request.args.get('teacherpassword')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from educator where teachername='" +
                   teachername + "' and teacherpassword='" + teacherpassword + "'")
    data = cursor.fetchone()
    if data is None:
        response = False
        response.status_code = 401
        return jsonify(response)  # "Username or Password is wrong"
    else:
        response = True
        response.status_code = 200
        return jsonify(response)  # "Logged in successfully"


@app.route('/api/educator/deleteeducator', methods=['POST'])
def deleteeducator():
    teacher_id = request.args.get('teacher_id')
    cursor = mysql.connect().cursor()
    cursor.execute("DELETE FROM educator WHERE id = %s", (teacher_id))
    mysql.connection.commit()
    cursor.close()
    response = 'successfully deleted educator'
    response.status_code = 200
    return jsonify(response)

# extra route to get all the data
@app.route('/api/educator/getalldata', methods=['GET'])
def getalldata():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * from educator")
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
