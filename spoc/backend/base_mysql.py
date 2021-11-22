import pymysql


class MySQL:

    def deletePostTheme(self, postThemeId):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM post " \
                      "WHERE id in (" \
                      "SELECT post_id from post_posttheme where posttheme_id=%s" \
                      ")"
        cursor.execute(instruction, [postThemeId])
        connection.commit()
        instruction = "DELETE FROM posttheme " \
                      "WHERE id=%s"
        cursor.execute(instruction, [postThemeId])
        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def deleteComment(self, commentId):
        connection, cursor = self.connectDatabase()

        instruction = "DELETE FROM comment " \
                      "where id=%s"
        cursor.execute(instruction, [commentId])
        connection.commit()
        self.closeDatabase(connection, cursor)
        return

    def deletePost(self, postId):
        connection, cursor = self.connectDatabase()

        # 这里只需要删除post，关系设置了外键，自动删除消失的post的关系
        instruction = "DELETE FROM post " \
                      "WHERE id=%s"
        cursor.execute(instruction, [postId])
        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getPostList(self, postThemeId):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT p.id, s.id, s.name, p.content, p.time FROM " \
                      "post as p, student_post as sp, student as s, post_posttheme as pp " \
                      "WHERE pp.posttheme_id=%s and pp.post_id=p.id and p.id=sp.post_id and sp.student_id=s.id " \
                      "ORDER by p.time desc"
        cursor.execute(instruction, [postThemeId])
        result = cursor.fetchall()
        self.closeDatabase(connection, cursor)
        return result

    def buildPost(self, postThemeId, userName, content, ti):
        connection, cursor = self.connectDatabase()
        instruction = "INSERT INTO post( content, time) " \
                      "values(%s, %s)"
        cursor.execute(instruction, [content, ti])
        connection.commit()

        instruction = "SELECT MAX(id) FROM post"

        cursor.execute(instruction)
        result = cursor.fetchall();
        result = result[0][0]

        instruction = "INSERT INTO student_post(student_id, post_id) " \
                      "VALUES (%s, %s)"
        cursor.execute(instruction, [userName, result])

        connection.commit()

        instruction = "INSERT INTO post_posttheme(posttheme_id, post_id) " \
                      "VALUES (%s, %s)"
        cursor.execute(instruction, [postThemeId, result])

        connection.commit()

        self.closeDatabase(connection, cursor)

        return

    def getPostThemeList(self):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT s.id, s.name, pt.title, pt.content, pt.time, pt.id FROM " \
                      "posttheme as pt, student_posttheme as sp, student as s " \
                      "WHERE pt.id=sp.posttheme_id AND sp.student_id=s.id " \
                      "ORDER BY pt.id"
        cursor.execute(instruction)
        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)
        return result

    def buildPostTheme(self, userName, title, content, ti):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO posttheme(title, content, time) " \
                      "values(%s, %s, %s)"
        cursor.execute(instruction, [title, content, ti])
        connection.commit()

        instruction = "SELECT MAX(id) FROM posttheme"

        cursor.execute(instruction)
        result = cursor.fetchall();
        result = result[0][0]

        instruction = "INSERT INTO student_posttheme(student_id, posttheme_id) " \
                      "VALUES (%s, %s)"
        cursor.execute(instruction, [userName, result])

        connection.commit()

        self.closeDatabase(connection, cursor)
        return

    def getCommentList(self, courseId):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT s.id, s.name, cc.c, cc.time, cc.id FROM " \
                      "(SELECT `time`, content, id FROM comment, course_comment as cc " \
                      "WHERE cc.course_id=%s and cc.comment_id=comment.id) AS cc(time,c,id), " \
                      "student_comment as sc, student AS s " \
                      "WHERE cc.id=sc.comment_id AND sc.student_id=s.id " \
                      "ORDER BY cc.time desc"

        cursor.execute(instruction, [courseId])
        result = cursor.fetchall()

        self.closeDatabase(connection, cursor)
        return result

    def commentCourse(self, courseId, userName, content, ti):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO comment(content, time) " \
                      "values(%s, %s)"

        cursor.execute(instruction, [content, ti])

        connection.commit()

        instruction = "SELECT MAX(id) FROM comment"

        cursor.execute(instruction)
        result = cursor.fetchall();
        result = result[0][0]

        instruction = "INSERT INTO student_comment(student_id, comment_id) " \
                      "VALUES (%s, %s)"

        cursor.execute(instruction, [userName, result])

        connection.commit()

        instruction = "INSERT INTO course_comment(course_id, comment_id) " \
                      "VALUES (%s, %s)"

        cursor.execute(instruction, [courseId, result])

        connection.commit()

        self.closeDatabase(connection, cursor)
        return

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

        instruction = "SELECT c.id, c.name, cm.material_id " \
                      "FROM " \
                      "(SELECT c.id, c.name " \
                      "FROM course AS c, student_course AS tc " \
                      "WHERE tc.student_id=%s AND c.id=tc.course_id " \
                      "ORDER BY c.id)" \
                      "AS c(id,name) " \
                      "LEFT OUTER JOIN course_material AS cm " \
                      "ON (c.id=cm.course_id)"

        # instruction = "SELECT c.id, c.name " \
        #               "FROM course AS c, student_course AS sc " \
        #               "WHERE c.id=sc.course_id AND sc.student_id=%s " \
        #               "ORDER BY c.id"

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

    def buildCourse(self, teacher_id, course_name, materialIdList):
        connection, cursor = self.connectDatabase()

        instruction = "INSERT INTO course(name) " \
                      "VALUES(%s)"
        cursor.execute(instruction, [course_name])
        connection.commit()

        instruction = "SELECT max(id) " \
                      "FROM course "
        cursor.execute(instruction)
        result = cursor.fetchall()

        course_id = result[0][0]

        instruction = "INSERT INTO teacher_course(teacher_id, course_id) " \
                      "VALUES(%s, %s)"

        cursor.execute(instruction, [teacher_id, course_id])
        connection.commit()

        if (materialIdList[0] != ''):

            for material_id in materialIdList:
                if material_id == "":
                    continue

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

    def changeCourse(self, teacher_id, course_id, course_name, materialIdList):
        connection, cursor = self.connectDatabase()
        instruction = "UPDATE course " \
                      "SET name=%s " \
                      "WHERE id=%s"
        cursor.execute(instruction, [course_name, course_id])
        connection.commit()

        # 找旧的课程资料id：
        instruction = "SELECT m.id " \
                      "FROM material AS m, course_material AS cm " \
                      "WHERE cm.material_id=m.id AND cm.course_id=%s"
        cursor.execute(instruction, [course_id])
        result = cursor.fetchall()

        print(result)
        print(materialIdList)
        for item in result:
            material_id = str(item[0])
            if materialIdList.count(material_id):
                materialIdList.remove(material_id)
            else:
                instruction = "DELETE FROM course_material " \
                              "WHERE course_id=%s AND material_id=%s"
                cursor.execute(instruction, [course_id, material_id])
                connection.commit()

        for material_id in materialIdList:
            if material_id == "":
                continue
            self.buildCourseMaterial(course_id, material_id)

        self.closeDatabase(connection, cursor)
        return

    def cancelCourse(self, teacher_id, course_id):
        connection, cursor = self.connectDatabase()

        # 不要删除课程对应的材料
        # instruction = "DELETE FROM material AS m " \
        #               "WHERE id IN " \
        #               "(" \
        #               "SELECT material_id " \
        #               "FROM course_material AS cm " \
        #               "WHERE cm.course_id=%s" \
        #               ")"
        # cursor.execute(instruction, [course_id])
        # connection.commit()
        instruction = "DELETE FROM comment " \
                      "WHERE id in (" \
                      "SELECT comment_id from course_comment WHERE course_id=%s" \
                      ")"
        cursor.execute(instruction, [course_id])
        connection.commit()

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

    def test(self):
        connection, cursor = self.connectDatabase()

        instruction = "SELECT MAX(id) FROM course "

        cursor.execute(instruction)

        result = cursor.fetchall()
        print(type(result[0][0]))

        self.closeDatabase(connection, cursor)
        return


if __name__ == "__main__":
    sql = MySQL()
    # sql.test()

    #
    # sql.commentCourse(1, 19373136, 1, "2021-20-22 11:12:22")
    #
    # result = sql.getCommentList("1")
    # commentList = []
    #
    # for item in result:
    #     commentList.append({"userName": item[0],
    #                         "userNickName": item[1],
    #                         "content": item[2],
    #                         "time": item[3]})
    #
    # print(commentList)
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
