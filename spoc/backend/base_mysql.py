import pymysql


def connect_database():
    connection = pymysql.connect(host="rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com",
                                 db="spoc",
                                 user="root",
                                 passwd="myja&*$4X579cKr",
                                 charset="utf8")
    cursor = connection.cursor()
    return connection, cursor


def find_student_course(userName, id):
    connection, cursor = connect_database()

    instruction = "SELECT *\
                FROM stu_course_list\
                Where username=%s AND id=%s"

    cursor.execute(instruction, [userName, id])

    result = cursor.fetchall()

    close_database(connection, cursor)
    return result


def select_course(userName, id):
    connection, cursor = connect_database()

    instruction = "INSERT INTO stu_course_list " \
                  "values(%s, %s)"

    cursor.execute(instruction, [userName, id])
    connection.commit()

    close_database(connection, cursor)

    return


def drop_student_course(userName, id):
    connection, cursor = connect_database()

    instruction = "DELETE FROM stu_course_list " \
                  "WHERE username=%s AND id=%s "
    cursor.execute(instruction, [userName, id])
    connection.commit()

    close_database(connection, cursor)
    return


def get_student_course(userName):
    connection, cursor = connect_database()

    instruction = "SELECT course.id, name " \
                  "FROM course, stu_course_list " \
                  "WHERE course.id=stu_course_list.id AND username=%s " \
                  "ORDER BY course.id"

    cursor.execute(instruction, [userName])

    result = cursor.fetchall()
    close_database(connection, cursor)

    return result


def get_all_course():
    connection, cursor = connect_database()

    instruction = "SELECT * " \
                  "FROM course"

    cursor.execute(instruction)
    result = cursor.fetchall()
    close_database(connection, cursor)
    return result


def close_database(connection, cursor):
    connection.close()
    cursor.close()


def create_student(userName, passWord):
    connection, cursor = connect_database()

    instruction = "INSERT INTO student " \
                  "values(%s, %s)"

    cursor.execute(instruction, [userName, passWord])
    connection.commit()

    close_database(connection, cursor)
    return


def create_teacher(userName, passWord):
    connection, cursor = connect_database()

    instruction = "INSERT INTO teacher " \
                  "values(%s, %s)"

    cursor.execute(instruction, [userName, passWord])
    connection.commit()

    close_database(connection, cursor)
    return


def find_teacher(userName):
    connection, cursor = connect_database()

    instruction = "SELECT *\
            FROM teacher\
            Where username=%s"

    cursor.execute(instruction, [userName])

    result = cursor.fetchall()

    close_database(connection, cursor)

    return result


def find_student(userName):
    connection, cursor = connect_database()

    instruction = "SELECT *\
            FROM student\
            Where username=%s"

    cursor.execute(instruction, [userName])

    result = cursor.fetchall()

    close_database(connection, cursor)

    return result


if __name__ == "__main__":
    userName = "19373136"

    drop_student_course(userName, "5")
    # select_course(userName, "2")
    result = get_student_course(userName)
    print(result)

    result = find_student_course(userName, "4")
    flag = not not result
    print(flag)
    """
    create table
    create_student = "CREATE TABLE `student` (`username` varchar(20) NOT NULL PRIMARY KEY, " \
                     "`password` varchar(32) NOT NULL);"
    
    try:
        cursor.execute(create_student)
    except Exception as e:
        print("exception occured: ", e)
    """
