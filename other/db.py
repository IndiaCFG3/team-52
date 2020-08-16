from flask import request, session
from flask import jsonify
from db_config import mysql
import re
from app import app
from doa import constants

@app.route('/api/educator/enternewgrades', methods=['POST'])
def enternewgrades():
    if request.method == "POST":
        student_id= request.form['student_id']
        month = request.form['month']
        parameters = request.form.getlist('parameters')
        score = list_to_score(parameters)
	
        cur = mysql.connection.cursor()
        sql = "INSERT INTO Student_Score(student_id, " + month.capitalize() + ") VALUES(%s, %s)"
        val = (student_id, score)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        response = 'successfully cread user in organization'
        response.status_code = 200
        
        return jsonify(response)


def get_average(month, teacher_id):
    cur = mysql.connection.cursor()
    sql = "SELECT " + month.capitalize() + "FROM Student_Score WHERE student_id IN " \
                                           "(SELECT student_id FROM Student WHERE teacher_id = " + teacher_id

    cur.execute(sql)

    n = constants.number_of_paramters
    p = [0]*n

    for x in cur:
        bin_format = '{0:0' + n + 'b}'
        score = bin_format.format(x)
        for i in range(n):
            p[i] += score[i]

    for i in range(n):
        p[i] = (p[i]/n)*100

    #Average list in percentage = p

    mysql.connection.commit()
    cur.close()
    response = 'successfully cread user in organization'
    response.status_code = 200

    return jsonify(response)







"SELECT " + month.capitalize() + "FROM Student_Score WHERE student_id IN (SELECT student_id FROM Student WHERE teacher_id = teacher_id)"



















