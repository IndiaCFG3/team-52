import mysql.connector
from constants import host, username as db_username, password as db_password, db


def validate_user(username, password, table):
    connection = mysql.connector.connect(host=host, username=db_username, password=db_password, database=db)
    cur = connection.cursor()

    sql = "SELECT * from User where Username='" + username + "' and Password='" + password + "' "
    cur.execute(sql)
    data = cur.fetchone()
    if data is None:
        return False
    return True
