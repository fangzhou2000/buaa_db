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
            print("请求登录的学生账号是%s,其正确密码是%s"%(result[0][0], result[0][1]))
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
            print("请求登录的教师账号是%s,其正确密码是%s"%(result[0][0], result[0][1]))
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
        # 从课程表里查询所有课程，返回一个字典的列表，字典中key值为 'name'
        result = get_course()
        print("GetCourseList")
        courses = [] # 字典列表
        for item in result:
            courses.append(dict([('id', item[0]),('name', item[1])]))
        return Response(courses)
