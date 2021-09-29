from django.db import models

import pymysql as mysql

class Student(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)

