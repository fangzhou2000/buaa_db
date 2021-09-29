from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class StudentLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("StudentLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 下面仅仅是模拟测试，需要从学生用户的表检索，不存在学号或学号为空返回1，密码错误返回2，登录成功返回0
        # todo
        if userName == "admin" and userPassWord == "123456":
            return Response(0)
        elif userName == "admin":
            return Response(2)
        else:
            return Response(1)


class StudentRegister(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))
        print("StudentRegister得到的学号和密码和确认密码是 " + userName + " " + userPassWord + " " + userPassWord2)
        # 下面仅仅是模拟测试，需要从学生用户的表中查询和写入，已存在学号返回1，密码不一致返回2，登录注册返回0
        # todo
        if userName == "admin":
            return Response(1)
        elif userPassWord != userPassWord2:
            return Response(2)
        else:
            return Response(0)


class TeacherLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("TeacherLogin得到的学号和密码是 " + userName + " " + userPassWord)
        # 下面仅仅是模拟测试，需要从教师用户的表检索，不存在工号或工号为空返回1，密码错误返回2，登录成功返回0
        # todo
        if userName == "admin1" and userPassWord == "123456":
            return Response(0)
        elif userName == "admin1":
            return Response(2)
        else:
            return Response(1)