from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .base_mysql import *


class StudentLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("StudentLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 下面仅仅是模拟测试，需要从学生用户的表检索，不存在学号或学号为空返回1，密码错误返回2，登录成功返回0
        # todo
        result = find_student(userName)
        flag = not not result

        if flag:
            print("请求登录的学生账号是%s,其正确密码是%s" % (result[0][0], result[0][1]))
        else:
            print("找不到该学生")

        if flag:
            if userPassWord == result[0][1]:
                return Response(0)
            else:
                return Response(2)
        else:
            return Response(1)


class StudentRegister(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))
        print("StudentRegister得到的学号和密码和确认密码是 " + userName + " " + userPassWord + " " + userPassWord2)
        # 下面仅仅是模拟测试，需要从学生用户的表中查询和写入，已存在学号返回1，密码不一致返回2，登成功返回0
        # todo

        result = find_student(userName)
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
            create_student(userName, userPassWord)
            return Response(0)


class TeacherLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("TeacherLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 下面仅仅是模拟测试，需要从教师用户的表检索，不存在工号或工号为空返回1，密码错误返回2，登录成功返回0
        # todo

        result = find_teacher(userName)
        flag = not not result

        if flag:
            print("请求登录的教师账号是%s,其正确密码是%s" % (result[0][0], result[0][1]))
        else:
            print("找不到该教师")

        if flag:
            if userPassWord == result[0][1]:
                return Response(0)
            else:
                return Response(2)
        else:
            return Response(1)

        # if userName == "admin" and userPassWord == "123456":
        #     return Response(0)
        # elif userName == "admin1":
        #     return Response(2)
        # else:
        #     return Response(1)


class TeacherRegister(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))
        print("TacherRegister得到的工号和密码和确认密码是 " + userName + " " + userPassWord + " " + userPassWord2)
        # 下面仅仅是模拟测试，需要从教师用户的表中查询和写入，已存在工号返回1，密码不一致返回2，登录成功返回0

        result = find_teacher(userName)
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
            create_teacher(userName, userPassWord)
            return Response(0)


class GetCourseList(APIView):
    def get(self, requset):
        # 从课程表里查询所有课程，返回一个字典的列表，字典中key值为 'id' 和 'name', id为主码
        result = get_all_course()
        print("GetCourseList")
        courses = []  # 字典列表
        for item in result:
            courses.append(dict([('id', item[0]), ('name', item[1])]))
        return Response(courses)


class SelectCourse(APIView):
    def get(self, request):
        # 从课程表里选择课程，先在学生选课表里查询该学生是否已经选了这个课程（通过userName和id），如果已有该课程，直接返回1，如果没有，则在学生选课表中添加该学生和该课程，并返回1
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))

        result = find_student_course(userName, id)
        flag = not not result
        # flag 表示是否有选课记录，True表示有选课记录。

        if flag:
            return Response(1)
        else:
            select_course(userName, id)
            return Response(0)
        # if 没选:
        #     return Response(0);
        # elif 选了:
        #     return Response(1);
        # else:
        #     //错误
        #     return Response(2);
        # 以上仅用于测试
        return Response(0)


class GetMyCourseList(APIView):
    def get(self, request):
        # 从学生选课表里查询该学生选的课
        userName = str(request.GET.get('userName', None))
        print('6666666666666666666')
        # 得到学生课程列表ok
        result = get_student_course(userName)
        myCourses = []  # 字典列表
        for item in result:
            myCourses.append(dict([("id", item[0]), ("name", item[1])]))
        print(myCourses)
        return Response(myCourses)


class DropCourse(APIView):
    def get(self, request):
        # 从学生选课表里删除该课程，然后再从学生选课表里查询该学生选的课，这里也可以考虑不返回，直接从前端删除，这个再讨论
        userName = str(request.GET.get('userName', None))
        id = str(request.GET.get('id', None))

        drop_student_course(userName, id)

        myCourses = []  # 字典列表

        result = get_student_course(userName)

        for item in result:
            myCourses.append(dict([("id", item[0]), ("name", item[1])]))

        return Response(myCourses)


class StudentChange(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))  # 学号
        userPassWord0 = str(request.GET.get('userPassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('userPassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('userPassWord2', None))  # 确认新密码
        # 从学生用户表里查， 如果原密码不正确返回1，如果正确，如果新密码不一致返回2，如果一致，在学生用户表里修改密码，返回0.
        return Response(0)


class TeacherChange(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))  # 学号
        userPassWord0 = str(request.GET.get('userPassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('userPassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('userPassWord2', None))  # 确认新密码
        # 从教师用户表里查， 如果原密码不正确返回1，如果正确，如果新密码不一致返回2，如果一致，在教师用户表里修改密码，返回0.
        return Response(0)


class BuildCourse(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        courseName = str(request.GET.get('userName', None))
        # 从课程表里新建课程，这里只提供了课程名称，需要在数据库里分配一个对于该课程唯一的id