import pymysql
from django.db import connection as con


def connect_database():
    connection = pymysql.connect(host="rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com",
                                 db="spoc",
                                 user="root",
                                 passwd="myja&*$4X579cKr",
                                 charset="utf8")
    cursor = connection.cursor()
    return connection, cursor

def get_course():


    connection, cursor = connect_database()

    instruction = "SELECT * " \
                  "FROM backend_course"

    cursor.execute(instruction)
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result

def close_database(connection, cursor):
    connection.close()
    cursor.close()

def create_student(userName, passWord):
    connection, cursor = connect_database()

    instruction = "INSERT INTO backend_student " \
                  "values(%s, %s)"

    cursor.execute(instruction, [userName, passWord])
    connection.commit()

    close_database(connection, cursor)
    return

def create_teacher(userName, passWord):
    connection, cursor = connect_database()

    instruction = "INSERT INTO backend_teacher " \
                  "values(%s, %s)"

    cursor.execute(instruction, [userName, passWord])
    connection.commit()

    close_database(connection, cursor)
    return

def find_teacher(userName):
    connection, cursor = connect_database()

    instruction = "SELECT *\
            FROM backend_teacher\
            Where username=%s"

    cursor.execute(instruction, [userName])

    result = cursor.fetchall()

    close_database(connection, cursor)

    return result

def find_student(userName):
    connection, cursor = connect_database()

    instruction = "SELECT *\
            FROM backend_student\
            Where username=%s"

    cursor.execute(instruction, [userName])

    result = cursor.fetchall()

    close_database(connection, cursor)

    return result

if __name__ == "__main__":
    connection, cursor = connect_database()
    userName = "19373136"
    instruction = "SELECT *\
            FROM backend_student\
            Where username=%s"

    print(instruction)

    cursor.execute(instruction, [userName])
    c = cursor.fetchall()

    print(c[0][0])

    print("running")

    close_database(connection, cursor)

"""
create table

create_student = "CREATE TABLE `backend_student` (`username` varchar(20) NOT NULL PRIMARY KEY, " \
                 "`password` varchar(32) NOT NULL);"

try:
    cursor.execute(create_student)
except Exception as e:
    print("exception occured: ", e)
"""
