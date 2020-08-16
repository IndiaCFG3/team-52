import mysql.connector
from constants import host, username as db_username, password as db_password, db


def create_user(username, password, table):
    try:
        connection = mysql.connector.connect(host=host, username=db_username, password=db_password, database=db)
        cur = connection.cursor()

        sql = "INSERT INTO " + table + "(username, password) VALUES (%s, %s)"

        cur.execute(sql, (username, password))
        connection.commit()

        cur.close()
        connection.close()
        return True

    except Exception as e:
        return False

