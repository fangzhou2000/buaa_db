from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class DataTest(APIView):
    def get(self,request,*args,**kwargs):
        print('请求后台数据成功！')
        return Response(['后台列表数据111','后台列表数据2'])
