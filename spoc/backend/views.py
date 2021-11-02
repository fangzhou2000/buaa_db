from rest_framework.views import APIView
from rest_framework.response import Response
from .base_mysql import MySQL


class StudentLogin(APIView):
    def get(self, request):
        # 默认userNickName为空
        # 需要将userNickName很久userName进行查找，赋值给userNickName。并返回前端（返回前端已完成）
        # userNickName = str(request.GET.get('userNickName', None))
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("StudentLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 需要从学生用户的表检索，不存在学号或学号为空返回1，密码错误返回2，登录成功返回0

        sql = MySQL()
        result = sql.findStudent(userName)
        flag = not not result

        if flag:
            print("请求登录的学生账号是%s,其正确密码是%s" % (result[0][0], result[0][1]))
            print("请求登录的学生姓名为%s" % result[0][2])
        else:
            print("找不到该学生")

        if flag:
            if userPassWord == result[0][1]:
                return Response(dict([('value', 0), ('userNickName', result[0][2])]))
            else:
                return Response(dict([('value', 2)]))
        else:
            return Response(dict([('value', 1)]))


class StudentRegister(APIView):
    def get(self, request):
        # 将userNickName保存在数据库中
        userNickName = str(request.GET.get('userNickName', None))
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))
        print("StudentRegister得到的学号和密码和确认密码是 " + userName + " " + userPassWord + " " + userPassWord2)
        # 需要从学生用户的表中查询和写入，已存在学号返回1，密码不一致返回2，登成功返回0

        sql = MySQL()
        result = sql.findStudent(userName)
        flag = not not result

        if flag:
            print("已经存在学生:" + userName)
        else:
            print("不存在该学生，可以注册:" + userName)

        if flag:  # 已经存在
            return Response(1)
        elif userPassWord != userPassWord2:
            return Response(2)
        else:
            # register一下nickname
            sql.registerStudent(userName, userPassWord, userNickName)
            return Response(0)


class TeacherLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("TeacherLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 需要从教师用户的表检索，不存在工号或工号为空返回1，密码错误返回2，登录成功返回0

        sql = MySQL()
        result = sql.findTeacher(userName)
        flag = not not result

        if flag:
            print("请求登录的教师账号是%s,其正确密码是%s\n" % (result[0][0], result[0][1]))
            print("请求的教师姓名为%s\n" %result[0][2])
        else:
            print("找不到该教师")

        if flag:
            if userPassWord == result[0][1]:
                return Response(dict([('value', 0), ('userNickName', result[0][2])]))
            else:
                return Response(dict([('value', 2)]))
        else:
            return Response(dict([('value', 1)]))



class TeacherRegister(APIView):
    def get(self, request):
        # 教师增加NickName
        userNickName = str(request.GET.get('userNickName', None))
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))
        print("TacherRegister得到的工号和密码和确认密码是 " + userName + " " + userPassWord + " " + userPassWord2)
        # 需要从教师用户的表中查询和写入，已存在工号返回1，密码不一致返回2，登录成功返回0

        sql = MySQL()

        result = sql.findTeacher(userName)
        flag = not not result

        if flag:
            print("已经存在教师:" + userName)
        else:
            print("不存在该教师，可以注册:" + userName)

        if flag:  # 已经存在
            return Response(1)
        elif userPassWord != userPassWord2:
            return Response(2)
        else:
            sql.registerTeacher(userName, userPassWord, userNickName)
            return Response(0)


class GetCourseList(APIView):
    def get(self, requset):
        # 从课程表里查询所有课程，返回一个字典的列表，字典中key值为 'id' 和 'name', id为主码
        print("GetCourseList请求得到所有课程")
        sql = MySQL()
        result = sql.getCourseList()
        courseList = []  # 字典列表
        for item in result:
            courseList.append(dict([('id', item[0]), ('name', item[1])]))
        return Response(courseList)


class SelectCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))
        # 从课程表里选择课程，先在学生选课表里查询该学生是否已经选了这个课程（通过userName和id），如果已有该课程，直接返回1，如果没有，则在学生选课表中添加该学生和该课程，并返回1
        print("TacherRegister得到的学号和课程id是 " + userName + " " + id)

        sql = MySQL()
        result = sql.findStudentCourse(userName, id)
        flag = not not result
        # flag 表示是否有选课记录，True表示有选课记录。

        if flag:
            return Response(1)
        else:
            sql.selectCourse(userName, id)
            return Response(0)


class GetStudentCourseList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        # 从学生选课表里查询该学生选的课
        print("GetMyCourseList得到的学号是 " + userName)

        sql = MySQL()
        result = sql.getStudentCourseList(userName)
        studentCourseList = []  # 字典列表
        for item in result:
            studentCourseList.append(dict([("id", item[0]), ("name", item[1])]))
        print(studentCourseList)
        return Response(studentCourseList)


class DropCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))
        # 从学生选课表里删除该课程，然后再从学生选课表里查询该学生选的课，这里也可以考虑不返回，直接从前端删除，这个再讨论
        print("DropCourse得到的学号和id是 " + userName + " " + id)

        sql = MySQL()
        sql.dropStudentCourse(userName, id)
        studentCourseList = []  # 字典列表
        result = sql.getStudentCourseList(userName)
        for item in result:
            studentCourseList.append(dict([("id", item[0]), ("name", item[1])]))
        return Response(studentCourseList)


class StudentChange(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))  # 学号
        userPassWord0 = str(request.GET.get('userPassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('userPassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('userPassWord2', None))  # 确认新密码
        # 从学生用户表里查， 如果原密码不正确返回1，如果正确，如果新密码不一致返回2，如果一致，在学生用户表里修改密码，返回0.
        print("StudentChange得到的学号和密码是 " + userName + " " + userPassWord0 + " " + userPassWord1 + " " + userPassWord2)

        sql = MySQL()
        result = sql.findStudent(userName)
        print(result)
        if userPassWord0 != result[0][1]:
            return Response(1)
        elif userPassWord2 != userPassWord1:
            return Response(2)
        else:
            sql.studentPasswordChange(userName, userPassWord1)
            return Response(0)


class TeacherChange(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))  # 学号
        userPassWord0 = str(request.GET.get('userPassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('userPassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('userPassWord2', None))  # 确认新密码
        # 从教师用户表里查， 如果原密码不正确返回1，如果正确，如果新密码不一致返回2，如果一致，在教师用户表里修改密码，返回0.
        print("TeacherChange得到的学号和密码是 " + userName + " " + userPassWord0 + " " + userPassWord1 + " " + userPassWord2)

        sql = MySQL()
        result = sql.findTeacher(userName)
        if userPassWord0 != result[0][1]:
            return Response(1)
        elif userPassWord2 != userPassWord1:
            return Response(2)
        else:
            sql.teacherPasswordChange(userName, userPassWord1)
            return Response(0)


class GetTeacherCourseList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        # 从课程表里查询该教师开设的课程，返回课程列表，（BuildCourse时会传入教师用户名，记录是哪个教师开的课。）

        sql = MySQL()
        result = sql.getTeacherCourseList(userName)
        teacherCourseList = []  # 字典列表
        print(result)
        for item in result:
            teacherCourseList.append(dict([('id', item[0]), ('name', item[1])]))
        return Response(teacherCourseList)


class BuildCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        course = request.GET.get('course', None)

        course = eval(course)

        # 从课程表里新建课程，这里只提供了课程名称，需要在数据库里分配一个对于该课程唯一的id
        print("BuildCourse得到的教师账号是 " + userName + "，课程名是:" + course['name'])
        print(course)
        sql = MySQL()
        sql.buildCourse(userName, course['name'], course['materialIdList'])
        return Response(0)


class GetCourseInfo(APIView):
    def get(self, request):
        return


class ChangeCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))
        # 教师改课程名，只能改自己开的课程的名，成功返回0

        sql = MySQL()
        name = "体育（5）"
        # 缺少更改后的课程名!!!!!!!!!!!!!!!！！！！！
        sql.changeCourseName(userName, id, name)
        return Response(0)


class CancelCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))
        # 教师停课，只能停自己开的课，成功返回0
        sql = MySQL()

        sql.cancelCourse(userName, id)
        return Response(0)

class GetMaterialList(APIView):
    def get(self, request):

        sql = MySQL()

        result = sql.getMaterialList()

        materialList = []
        for item in result:
            materialList.append(dict([('id', item[0]), ('name', item[1])]))
        return Response(materialList)

class BuildMaterial(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        materialName = str(request.GET.get('materialName', None))

        sql = MySQL()

        sql.buildMaterial(userName, materialName)

        return Response(0)


class GetTeacherMaterialList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))

        sql = MySQL()

        result = sql.getTeacherMaterialList(userName)
        teacherMaterialList = []

        for item in result:
            teacherMaterialList.append(dict([('id', item[0]), ('name', item[1])]))
        return Response(teacherMaterialList)

class DeleteMaterial(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))

        sql = MySQL()

        sql.deleteMaterial(userName, id)

        return Response(0)