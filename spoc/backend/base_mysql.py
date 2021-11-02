import pymysql


class MySQL:

    def getMaterialName(self, material_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT name " \
                      "FROM material " \
                      "WHERE id=%s"
        cursor.execute(instruction, [material_id])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)
        return result

    def deleteMaterial(self, teached_id, material_id):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM material " \
                      "WHERE id=%s"

        cursor.execute(instruction, [material_id])

        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getTeacherMaterialList(self, teacher_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT m.id, m.name " \
                      "FROM material AS m, teacher_material AS tm " \
                      "WHERE tm.teacher_id=%s AND tm.material_id=m.id"

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

        instruction = "INSERT INTO material(name) " \
                      "VALUES(%s) "

        cursor.execute(instruction, [materialName])
        connection.commit()

        instruction = "SELECT id " \
                      "FROM material " \
                      "WHERE name=%s"

        cursor.execute(instruction, [materialName])
        result = cursor.fetchall()

        material_id = result[len(result) - 1][0]

        instruction = "INSERT INTO teacher_material(teacher_id, material_id) " \
                      "VALUES(%s, %s)"
        cursor.execute(instruction, [teacher_id, material_id])
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

    def findStudentCourse(self, student_id, course_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                    FROM student_course\
                    Where student_id=%s AND course_id=%s"

        cursor.execute(instruction, [student_id, course_id])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)
        return result

    def selectCourse(self, student_id, course_id):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO student_course(student_id, course_id) " \
                      "values(%s, %s)"

        cursor.execute(instruction, [student_id, course_id])
        connection.commit()

        self.closeDatabase(connection, cursor)

        return

    def dropStudentCourse(self, student_id, course_id):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM student_course " \
                      "WHERE student_id=%s AND course_id=%s "
        cursor.execute(instruction, [student_id, course_id])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getTeacherCourseList(self, teacher_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT c.id, c.name, cm.material_id " \
                      "FROM " \
                      "(SELECT c.id, c.name " \
                      "FROM course AS c, teacher_course AS tc " \
                      "WHERE tc.teacher_id=%s AND c.id=tc.course_id " \
                      "ORDER BY c.id)" \
                      "AS c(id,name) " \
                      "LEFT OUTER JOIN course_material AS cm " \
                      "ON (c.id=cm.course_id)"

        cursor.execute(instruction, [teacher_id])
        return cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def getStudentCourseList(self, student_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT c.id, c.name " \
                      "FROM course AS c, student_course AS sc " \
                      "WHERE c.id=sc.course_id AND sc.student_id=%s " \
                      "ORDER BY c.id"

        cursor.execute(instruction, [student_id])

        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def getCourseList(self):
        connection, cursor = self.connectDatabase()

        # instruction = "SELECT c.id, c.name, cm.material_id " \
        #               "FROM course AS c, course_material AS cm " \
        #               "WHERE c.id=cm.course_id"
        instruction = "SELECT c.id, c.name, cm.material_id " \
                      "FROM course AS c LEFT OUTER JOIN course_material AS cm " \
                      "ON (c.id=cm.course_id)"

        cursor.execute(instruction)
        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def buildCourseMaterial(self, course_id, material_id):
        connection, cursor = self.connectDatabase()
        instruction = "INSERT INTO course_material(material_id, course_id) " \
                      "VALUES(%s, %s)"
        cursor.execute(instruction, [material_id, course_id])
        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def buildCourse(self, teacher_id, course_name, materialList):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO course(name) " \
                      "VALUES(%s)"
        cursor.execute(instruction, [course_name])
        connection.commit()

        instruction = "SELECT id " \
                      "FROM course " \
                      "WHERE name=%s"
        cursor.execute(instruction, [course_name])
        result = cursor.fetchall()

        course_id = result[len(result) - 1][0]

        instruction = "INSERT INTO teacher_course(teacher_id, course_id) " \
                      "VALUES(%s, %s)"

        cursor.execute(instruction, [teacher_id, course_id])
        connection.commit()

        if (materialList[0] != ''):

            for material in materialList:
                if material == "":
                    continue
                self.buildMaterial(teacher_id, material)
                instruction = "SELECT id " \
                              "FROM material " \
                              "WHERE name=%s"
                cursor.execute(instruction, [material])
                result = cursor.fetchall()

                material_id = result[len(result) - 1][0]

                self.buildCourseMaterial(course_id, material_id)

        self.closeDatabase(connection, cursor)

        return

    def closeDatabase(self, connection, cursor):
        connection.close()
        cursor.close()

    def registerStudent(self, student_id, password, student_name):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO student " \
                      "values(%s, %s, %s)"

        cursor.execute(instruction, [student_id, password, student_name])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def registerTeacher(self, teacher_id, password, teacher_name):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO teacher " \
                      "values(%s, %s, %s)"

        cursor.execute(instruction, [teacher_id, password, teacher_name])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def findTeacher(self, teacher_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                FROM teacher\
                Where id=%s"

        cursor.execute(instruction, [teacher_id])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def findStudent(self, student_id):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT *\
                FROM student\
                Where id=%s"

        cursor.execute(instruction, [student_id])

        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)

        return result

    def studentPasswordChange(self, student_id, password):
        connection, cursor = self.connectDatabase()

        instruction = "UPDATE student " \
                      "SET password=%s " \
                      "WHERE id=%s"
        cursor.execute(instruction, [password, student_id])

        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def changeCourse(self, teacher_id, course_id, course_name, materialList):
        connection, cursor = self.connectDatabase()
        instruction = "UPDATE course " \
                      "SET name=%s " \
                      "WHERE id=%s"
        cursor.execute(instruction, [course_name, course_id])
        connection.commit()

        # 找旧的课程资料：
        instruction = "SELECT m.id, m.name " \
                      "FROM material AS m, course_material AS cm " \
                      "WHERE cm.material_id=m.id AND cm.course_id=%s"
        cursor.execute(instruction, [course_id])
        result = cursor.fetchall()

        for item in result:
            if materialList.count(item[1]):
                materialList.remove(item[1])
                pass
            else:
                instruction = "DELETE FROM material " \
                              "WHERE id=%s"
                cursor.execute(instruction, [item[0]])
                connection.commit()
        for material in materialList:
            if material == "":
                continue
            self.buildMaterial(teacher_id, material)
            instruction = "SELECT id " \
                          "FROM material " \
                          "WHERE name=%s"
            cursor.execute(instruction, [material])
            result = cursor.fetchall()

            material_id = result[len(result) - 1][0]

            self.buildCourseMaterial(course_id, material_id)

        self.closeDatabase(connection, cursor)
        return

    def cancelCourse(self, teacher_id, course_id):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM course " \
                      "WHERE id=%s"

        cursor.execute(instruction, [course_id])
        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def teacherPasswordChange(self, teacher_id, password):
        connection, cursor = self.connectDatabase()

        instruction = "UPDATE teacher " \
                      "SET password=%s " \
                      "WHERE id=%s"
        cursor.execute(instruction, [password, teacher_id])

        connection.commit()
        self.closeDatabase(connection, cursor)
        return


if __name__ == "__main__":
    s = "1,2，3"
    s.s
    s = s.split("[,]")
    print(s)
    # sql = MySQL()
    # # sql.buildMaterial("123", "234")
    # result = sql.getMaterialList()
    # print(result)
    #
    # result = sql.getTeacherMaterialList("123")
    # print(result)
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
