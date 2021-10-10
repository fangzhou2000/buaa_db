import pymysql


class baseSQL:

    def connect_database(self):
        connection = pymysql.connect(host="rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com",
                                     db="spoc",
                                     user="root",
                                     passwd="myja&*$4X579cKr",
                                     charset="utf8")
        cursor = connection.cursor()
        return connection, cursor

    def find_student_course(self, userName, id):
        connection, cursor = self.connect_database()

        instruction = "SELECT *\
                    FROM stu_course_list\
                    Where username=%s AND id=%s"

        cursor.execute(instruction, [userName, id])

        result = cursor.fetchall()

        self.close_database(connection, cursor)
        return result

    def select_course(self, userName, id):
        connection, cursor = self.connect_database()

        instruction = "INSERT INTO stu_course_list " \
                      "values(%s, %s)"

        cursor.execute(instruction, [userName, id])
        connection.commit()

        self.close_database(connection, cursor)

        return

    def drop_student_course(self, userName, id):
        connection, cursor = self.connect_database()

        instruction = "DELETE FROM stu_course_list " \
                      "WHERE username=%s AND id=%s "
        cursor.execute(instruction, [userName, id])
        connection.commit()

        self.close_database(connection, cursor)
        return

    def get_student_course(self, userName):
        connection, cursor = self.connect_database()

        instruction = "SELECT course.id, name " \
                      "FROM course, stu_course_list " \
                      "WHERE course.id=stu_course_list.id AND username=%s " \
                      "ORDER BY course.id"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()
        self.close_database(connection, cursor)

        return result

    def get_all_course(self):
        connection, cursor = self.connect_database()

        instruction = "SELECT * " \
                      "FROM course"

        cursor.execute(instruction)
        result = cursor.fetchall()
        self.close_database(connection, cursor)
        return result

    def create_course(self, userName, courseName):
        connection, cursor = self.connect_database()

        instruction = "INSERT INTO course(name) " \
                      "VALUES(%s)"
        cursor.execute(instruction, [courseName])

        connection.commit()

        self.close_database(connection, cursor)

    def close_database(self, connection, cursor):
        connection.close()
        cursor.close()

    def create_student(self, userName, passWord):
        connection, cursor = self.connect_database()

        instruction = "INSERT INTO student " \
                      "values(%s, %s)"

        cursor.execute(instruction, [userName, passWord])
        connection.commit()

        self.close_database(connection, cursor)
        return

    def create_teacher(self, userName, passWord):
        connection, cursor = self.connect_database()

        instruction = "INSERT INTO teacher " \
                      "values(%s, %s)"

        cursor.execute(instruction, [userName, passWord])
        connection.commit()

        self.close_database(connection, cursor)
        return

    def find_teacher(self, userName):
        connection, cursor = self.connect_database()

        instruction = "SELECT *\
                FROM teacher\
                Where username=%s"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()

        self.close_database(connection, cursor)

        return result

    def find_student(self, userName):
        connection, cursor = self.connect_database()

        instruction = "SELECT *\
                FROM student\
                Where username=%s"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()

        self.close_database(connection, cursor)

        return result

    def change_stu_password(self, userName, passWord):
        connection, cursor = self.connect_database()

        instruction = "UPDATE student " \
                      "SET password=%s " \
                      "WHERE username=%s"
        cursor.execute(instruction, [passWord, userName])

        connection.commit()
        self.close_database(connection, cursor)
        return

    def change_teacher_password(self, userName, passWord):
        connection, cursor = self.connect_database()

        instruction = "UPDATE teacher " \
                      "SET password=%s " \
                      "WHERE username=%s"
        cursor.execute(instruction, [passWord, userName])

        connection.commit()
        self.close_database(connection, cursor)
        return


if __name__ == "__main__":
    userName = "19373136"
    sql = baseSQL()
    sql.drop_student_course(userName, "5")
    # select_course(userName, "2")
    result = sql.get_student_course(userName)
    print(result)

    result = sql.find_student_course(userName, "4")
    flag = not not result
    print(flag)
    sql.change_teacher_password("123", "123456")
    # sql.create_course("13","线性代数2")
    """
    create table
    create_student = "CREATE TABLE `student` (`username` varchar(20) NOT NULL PRIMARY KEY, " \
                     "`password` varchar(32) NOT NULL);"
    
    try:
        cursor.execute(create_student)
    except Exception as e:
        print("exception occured: ", e)
    """
