import mysql.connector
from constants import host, username as db_username, password as db_password, db


def insert_score(student_id, score, month):
    try:
        connection = mysql.connector.connect(host=host, username=db_username, password=db_password, database=db)
        cur = connection.cursor()

        sql = "INSERT INTO Student_Score(student_id, " + month + ") VALUES (%s, %s)"

        cur.execute(sql, (student_id, score))
        connection.commit()

        cur.close()
        connection.close()
        print("Done!")

    except Exception as e:
        print("Error!")

