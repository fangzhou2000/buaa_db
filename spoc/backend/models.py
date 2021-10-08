from django.db import models

import pymysql

# 这些可以删除，但不要执行migrate
class Student(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)

class teacher(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)