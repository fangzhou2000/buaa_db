import pymysql

connection = pymysql.connect(host="rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com",
                             db="spoc",
                             user="root",
                             passwd="myja&*$4X579cKr",
                             charset="utf8")
cursor = connection.cursor()

""" create table

create_student = "CREATE TABLE `backend_student` (`username` varchar(20) NOT NULL PRIMARY KEY, " \
                 "`password` varchar(32) NOT NULL);"

try:
    cursor.execute(create_student)
except Exception as e:
    print("exception occured: ", e)

"""

connection.close()
