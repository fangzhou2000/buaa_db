from rest_framework.views import APIView
from rest_framework.response import Response
from .base_mysql import MySQL

class GetPostTheme(APIView):
    def get(self, request):
        postThemeId = str(request.GET.get('postThemeId', None))
        sql = MySQL()
        r = sql.getPostTheme(postThemeId)
        dic = {"id": r[0][0], "userName": r[1][0], "userNickName": r[1][1],
               "title": r[0][1], "content": r[0][2], "time": r[0][3],
               "isTeacher": r[0][4]}
        print(dic)
        return Response(dic)

class AdminChange(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))  # 管理员账号
        userPassWord0 = str(request.GET.get('userPassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('userPassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('userPassWord2', None))  # 确认新密码
        sql = MySQL()
        result = sql.findAdmin(userName)
        print(result)
        if userPassWord0 != result[0][1]:
            return Response(1)
        elif userPassWord2 != userPassWord1:
            return Response(2)
        else:
            sql.adminChange(userName, userPassWord1)
            return Response(0)


class GetTeacherList(APIView):
    def get(self, request):
        sql = MySQL()
        result = sql.getTeacherList()

        teacherList = []
        for item in result:
            teacherList.append(dict([("id", item[0]), ("name", item[1])]))
        print(teacherList)
        return Response(teacherList)


class GetStudentList(APIView):
    def get(self, request):
        sql = MySQL()
        result = sql.getStudentList()

        studentList = []
        for item in result:
            studentList.append(dict([("id", item[0]), ("name", item[1])]))
        print(studentList)
        return Response(studentList)


class AdminLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))

        sql = MySQL()
        result = sql.findAdmin(userName)
        flag = not not result

        if flag:
            # 有该管理员
            if userPassWord == result[0][1]:
                return Response(dict([('value', 0), ('userNickName', result[0][2])]))
            else:
                return Response(dict([('value', 2)]))
        else:
            return Response(dict([('value', 1)]))


class DeletePostTheme(APIView):
    def get(self, request):
        postThemeId = str(request.GET.get("postThemeId", None))
        sql = MySQL()
        sql.deletePostTheme(postThemeId)
        return Response(0)


class DeletePost(APIView):
    def get(self, request):
        postId = str(request.GET.get("postId", None))
        sql = MySQL()
        sql.deletePost(postId)
        return Response(0)


class DeleteComment(APIView):
    def get(self, request):
        commentId = str(request.GET.get("commentId", None))
        sql = MySQL()
        sql.deleteComment(commentId)
        return Response(0)


class BuildPost(APIView):
    def get(self, request):
        postThemeId = str(request.GET.get("postThemeId", None))
        userName = str(request.GET.get("userName", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))

        isTeacher = str(request.GET.get("isTeacher", None))
        # isTeacher = 1 if isTeacher == "true" else 0

        sql = MySQL()
        sql.buildPost(postThemeId, userName, content, time, isTeacher)
        return Response(0)


class GetPostList(APIView):
    def get(self, request):
        postThemeId = str(request.GET.get("postThemeId", None))
        print(postThemeId)
        sql = MySQL()
        result = sql.getPostList(postThemeId)
        postList = []

        for i in result:
            postList.append({"id": i[0],
                             "userName": i[1],
                             "userNickName": i[2],
                             "content": i[3],
                             "time": i[4],
                             "isTeacher": i[5]})
        postList.sort(key=lambda x: x['time'], reverse=True)
        print(postList)
        return Response(postList)


class BuildPostTheme(APIView):
    def get(self, request):
        userName = str(request.GET.get("userName", None))
        title = str(request.GET.get("title", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))
        isTeacher = str(request.GET.get("isTeacher", None))

        sql = MySQL()
        sql.buildPostTheme(userName, title, content, time, isTeacher)

        return Response(0)


class GetPostThemeList(APIView):
    def get(self, request):
        sql = MySQL()
        result = sql.getPostThemeList()
        postThemeList = []

        for i in result:
            postThemeList.append({"id": i[5],
                                  "userName": i[0],
                                  "userNickName": i[1],
                                  "title": i[2],
                                  "content": i[3],
                                  "time": i[4],
                                  "isTeacher": i[6]})
        postThemeList.sort(key=lambda x: x['id'], reverse=True)
        return Response(postThemeList)


class GetCommentList(APIView):
    def get(self, request):
        courseId = str(request.GET.get("courseId", None))
        sql = MySQL()
        result = sql.getCommentList(courseId)

        commentList = []

        for item in result:
            commentList.append({"id": item[4],
                                "userName": item[0],
                                "userNickName": item[1],
                                "content": item[2],
                                "time": item[3]})
        commentList.sort(key=lambda x: x['time'], reverse=True)
        return Response(commentList)


class CommentCourse(APIView):
    def get(self, request):
        # String courseId, String userName, String userNickName, String content, String time
        courseId = str(request.GET.get("courseId", None))
        userName = str(request.GET.get("userName", None))
        userNickName = str(request.GET.get("userNickName", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))
        degree = str(request.GET.get('degree', None))

        sql = MySQL()
        sql.commentCourse(courseId, userName, content, time, degree)

        return Response(0)


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
            print("请求的教师姓名为%s\n" % result[0][2])
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
            courseList.append({'id': item[0], 'name': item[1], 'teacherName': item[2], 'introduction': item[5] if
            item[5] is not None else '', 'materialList': [], 'm_id': item[3] if item[3] is not None else '',
                               'm_name': item[4] if item[4] is not None else ''})
        courseList.sort(key=lambda x: x['id'], reverse=False)
        i = 0
        while i < len(courseList):
            if courseList[i]['m_id'] != '' and len(courseList[i]['materialList']) == 0:
                courseList[i]['materialList'].append({'id': courseList[i]['m_id'], 'name': courseList[i]['m_name']});

            if i != len(courseList) - 1 and courseList[i]['id'] == courseList[i + 1]['id']:
                courseList[i]['materialList'].append(
                    {'id': courseList[i + 1]['m_id'], 'name': courseList[i + 1]['m_name']});
                courseList.pop(i + 1)
                i -= 1
            i += 1

        for item in courseList:
            print(item['materialList'], end=" ")
            print(item['id'], item['name'], item['teacherName'], item['introduction'])

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
            studentCourseList.append({'id': item[0], 'name': item[1], 'teacherName': item[2], 'introduction': item[5] if
            item[5] is not None else '', 'materialList': [], 'm_id': item[3] if item[3] is not None else '',
                                      'm_name': item[4] if item[4] is not None else ''})
        studentCourseList.sort(key=lambda x: x['id'])
        i = 0
        while i < len(studentCourseList):
            if studentCourseList[i]['m_id'] != '' and len(studentCourseList[i]['materialList']) == 0:
                studentCourseList[i]['materialList'].append(
                    {'id': studentCourseList[i]['m_id'], 'name': studentCourseList[i]['m_name']});

            if i != len(studentCourseList) - 1 and studentCourseList[i]['id'] == studentCourseList[i + 1]['id']:
                studentCourseList[i]['materialList'].append(
                    {'id': studentCourseList[i + 1]['m_id'], 'name': studentCourseList[i + 1]['m_name']});
                studentCourseList.pop(i + 1)
                i -= 1
            i += 1

        for item in studentCourseList:
            print(item['materialList'], end=" ")
            print(item['id'], item['name'], item['teacherName'], item['introduction'])

        return Response(studentCourseList)


class DropCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))
        # 从学生选课表里删除该课程，然后再从学生选课表里查询该学生选的课，这里也可以考虑不返回，直接从前端删除，这个再讨论
        print("DropCourse得到的学号和id是 " + userName + " " + id)

        sql = MySQL()
        sql.dropStudentCourse(userName, id)
        # studentCourseList = []  # 字典列表
        # result = sql.getStudentCourseList(userName)
        # for item in result:
        #     studentCourseList.append({'id': item[0], 'name': item[1]})
        return Response(0)


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

        for item in result:
            teacherCourseList.append({'id': item[0], 'name': item[1], 'teacherName': item[2], 'introduction': item[5] if
            item[5] is not None else '', 'materialList': [], 'm_id': item[3] if item[3] is not None else '',
                                      'm_name': item[4] if item[4] is not None else ''})

        teacherCourseList.sort(key=lambda x: x['id'])
        i = 0
        while i < len(teacherCourseList):
            if teacherCourseList[i]['m_id'] != '' and len(teacherCourseList[i]['materialList']) == 0:
                teacherCourseList[i]['materialList'].append(
                    {'id': teacherCourseList[i]['m_id'], 'name': teacherCourseList[i]['m_name']});

            if i != len(teacherCourseList) - 1 and teacherCourseList[i]['id'] == teacherCourseList[i + 1]['id']:
                teacherCourseList[i]['materialList'].append(
                    {'id': teacherCourseList[i + 1]['m_id'], 'name': teacherCourseList[i + 1]['m_name']});
                teacherCourseList.pop(i + 1)
                i -= 1
            i += 1

        for item in teacherCourseList:
            print(item['materialList'], end=" ")
            print(item['id'], item['name'], item['teacherName'], item['introduction'])
        return Response(teacherCourseList)


class GetCourseInfo(APIView):
    def get(self, request):
        return


class BuildCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        course = request.GET.get('course', None)

        course = eval(course)

        # 从课程表里新建课程，这里只提供了课程名称，需要在数据库里分配一个对于该课程唯一的id
        print("BuildCourse得到的教师账号是 " + userName + "，课程名是:" + course['name'])
        print(course)
        if course['name'] == "":
            return Response(2)

        sql = MySQL()
        for item in course['materialIdList']:
            if item == '':
                continue
            if not sql.getMaterialName(item):
                return Response(1)

        sql.buildCourse(userName, course['name'], course['materialIdList'], course['introduction'])
        return Response(0)


class ChangeCourse(APIView):
    def get(self, request):
        course_id = str(request.GET.get('id', None))
        course_name = str(request.GET.get('name', None))
        introduction = str(request.GET.get('introduction', None))
        teacher_id = str(request.GET.get('userName', None))

        materialIdString = str(request.GET.get('materialIdString', None))

        print(materialIdString)

        materialIdList = materialIdString.split(',')

        # course = request.GET.get('course', None)
        # 教师改课程名，只能改自己开的课程的名，成功返回0
        # course = eval(course)

        if course_name == '':
            return Response(2)

        sql = MySQL()

        for item in materialIdList:
            if item == '':
                continue
            if not sql.getMaterialName(item):
                return Response(1)
        sql.changeCourse(teacher_id, course_id, course_name, materialIdList, introduction)
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
            materialList.append({'id': item[0], 'name': item[1]})
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
            teacherMaterialList.append({'id': item[0], 'name': item[1]})
        return Response(teacherMaterialList)


class DeleteMaterial(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))

        sql = MySQL()

        sql.deleteMaterial(userName, id)

        return Response(0)


class GetStudentCourseNum(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        # 传入学生的学号
        sql = MySQL()
        result = sql.getStudentCourseNum(userName)
        # ((0,),)
        return Response(result[0][0])
        # 返回一个courseNum


class GetStudentCommentNum(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        sql = MySQL()
        result = sql.getStudentCommentNum(userName)
        return Response(result[0][0])
        # 同上，返回commentNum


class GetStudentDiscussNum(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        sql = MySQL()
        result = sql.getStudentDiscussNum(userName)
        return Response(result[0][0])


class GetTeacherCourseNum(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        # 传入老师工号
        sql = MySQL()
        result = sql.getTeacherCourseNum(userName)
        return Response(result[0][0])
        # 返回开设课程数


class GetTeacherDisCussNum(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        # 传入老师工号
        sql = MySQL()
        result = sql.getTeacherDisCussNum(userName)
        return Response(result[0][0])
        # 返回评论数目


class PushDegree(APIView):
    def get(self, request):
        # 课程id
        id = str(request.GET.get('id', None))

        # 传入的评价等级分为1,2,3,4,5五个
        # 只能是这五个
        degree = str(request.GET.get('degree', None))
        userName = str(request.GET.get('userName', None))

        # 将评价人的评价（1，2,3，4,5）存在对应的表中   (if)
        # 不用返回


class GetDegree(APIView):
    def get(self, request):
        id = str(request.GET.get('id', None))
        id = int(id)
        sql = MySQL()
        result = sql.getCourseDegree(id);
        # 返回课程对应的评价表，计算平均值交给前端
        # 评价表为{1：float， 2：float， 3：float， 4：float， 5：float, totalNum: number, avgDegree(平均分): float}
        # print(result)
        dic = {"1": result[0][1], "2": result[0][2], "3": result[0][3],
               "4": result[0][4], "5": result[0][5], "totalNum": result[0][6],
               "avgDegree": result[0][7]}
        print(dic)
        return Response(dic)
