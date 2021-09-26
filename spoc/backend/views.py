from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class Login(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("后台得到的用户名和密码是 " + userName + " " + userPassWord)
        # 下面仅仅是模拟测试，需要从数据库检索，不存在用户名或用户名为空返回1，密码错误返回2，登录成功返回0
        if userName == "admin" and userPassWord == "123456":
            return Response(0)
        elif userName == "admin":
            return Response(2)
        else:
            return Response(1)