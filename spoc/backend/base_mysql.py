import pymysql


class MySQL:

    def deleteMaterial(self, teached_id, id):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM material " \
                      "WHERE teacher_id=%s AND id=%s"

        cursor.execute(instruction, [teached_id, id])

        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getTeacherMaterialList(self, teacher_id):
        connection, cursor = self.connectDatabase()
        instruction = "SELECT id, name " \
                      "FROM material " \
                      "WHERE teacher_id=%s"

        cursor.execute(instruction, [teacher_id])

        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def getMaterialList(self):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT id, name " \
                      "FROM material "

        cursor.execute(instruction)

        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def buildMaterial(self, teacher_id, materialName):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO material(name, teacher_id) " \
                      "VALUES(%s, %s) "

        cursor.execute(instruction, [materialName, teacher_id])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def connectDatabase(self):
        connection = pymysql.connect(host="rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com",
                                     db="spoc",
                                     user="root",
                                     passwd="myja&*$4X579cKr",
                                     charset="utf8")
        cursor = connection.cursor()
        return connection, cursor

    def findStudentCourse(self, userName, id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                    FROM stu_course_list\
                    Where username=%s AND id=%s"

        cursor.execute(instruction, [userName, id])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)
        return result

    def selectCourse(self, userName, id):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO stu_course_list " \
                      "values(%s, %s)"

        cursor.execute(instruction, [userName, id])
        connection.commit()

        self.closeDatabase(connection, cursor)

        return

    def dropStudentCourse(self, userName, id):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM stu_course_list " \
                      "WHERE username=%s AND id=%s "
        cursor.execute(instruction, [userName, id])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getTeacherCourseList(self, userName):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT * FROM course " \
                      "WHERE teacher_id=%s"
        cursor.execute(instruction, [userName])
        return cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def getStudentCourseList(self, userName):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT c.id, name " \
                      "FROM course AS c, stu_course_list AS scl " \
                      "WHERE c.id=scl.id AND username=%s " \
                      "ORDER BY c.id"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)

        return result

    def getCourseList(self):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT * " \
                      "FROM course"

        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def buildCourse(self, userName, courseName):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO course(name, teacher_id) " \
                      "VALUES(%s, %s)"
        cursor.execute(instruction, [courseName, userName])

        connection.commit()

        self.closeDatabase(connection, cursor)

    def closeDatabase(self, connection, cursor):
        connection.close()
        cursor.close()

    def registerStudent(self, userName, passWord, name):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO student " \
                      "values(%s, %s, %s)"

        cursor.execute(instruction, [userName, passWord, name])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def registerTeacher(self, userName, passWord, name):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO teacher " \
                      "values(%s, %s, %s)"

        cursor.execute(instruction, [userName, passWord, name])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def findTeacher(self, userName):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                FROM teacher\
                Where username=%s"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def findStudent(self, userName):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                FROM student\
                Where username=%s"

        cursor.execute(instruction, [userName])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def studentPasswordChange(self, userName, passWord):
        connection, cursor = self.connectDatabase()

        instruction = "UPDATE student " \
                      "SET password=%s " \
                      "WHERE username=%s"
        cursor.execute(instruction, [passWord, userName])

        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def changeCourseName(self, teacherID, courseID, courseName):
        connection, cursor = self.connectDatabase()
        instruction = "UPDATE course " \
                      "SET name=%s " \
                      "WHERE id=%s AND teacher_id=%s"

        cursor.execute(instruction, [courseName, courseID, teacherID])

        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def cancelCourse(self, teacherID, courseID):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM course " \
                      "WHERE teacher_id=%s AND id=%s"

        cursor.execute(instruction, [teacherID, courseID])
        connection.commit()
        self.closeDatabase(connection, cursor)

        result = self.getTeacherCourseList(teacherID)

        return result

    def teacherPasswordChange(self, userName, passWord):
        connection, cursor = self.connectDatabase()

        instruction = "UPDATE teacher " \
                      "SET password=%s " \
                      "WHERE username=%s"
        cursor.execute(instruction, [passWord, userName])

        connection.commit()
        self.closeDatabase(connection, cursor)
        return


if __name__ == "__main__":
    sql = MySQL()
    # sql.buildMaterial("123", "234")
    result = sql.getMaterialList()
    print(result)

    result = sql.getTeacherMaterialList("123")
    print(result)
    """
    userName = "19373136"
    sql = MySQL()
    sql.dropStudentCourse(userName, "5")
    # select_course(userName, "2")
    result = sql.getStudentCourseList(userName)
    print(result)

    result = sql.findStudentCourse(userName, "4")
    flag = not not result
    print(flag)
    sql.teacherPasswordChange("123", "123456")
    # sql.create_course("13","线性代数2")
    """

    """
    create table
    create_student = "CREATE TABLE `student` (`username` varchar(20) NOT NULL PRIMARY KEY, " \
                     "`password` varchar(32) NOT NULL);"
    
    try:
        cursor.execute(create_student)
    except Exception as e:
        print("exception occured: ", e)
    """
