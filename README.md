# BUAA DB

2021年北航数据库大作业


## Description 
 [![](https://img.shields.io/badge/frontend-Vue.js-informational)](https://vuejs.org/)   [![](https://img.shields.io/badge/backend-Django-informational)](https://www.djangoproject.com/) 

### build and run：

```shell
$ cd spoc
$ python manage.py runserver
```

## Task List

Vue架构、前后端接口 (tqj)

Vue样式 (oyk)

<details>
<summary>Django后端、MySQL (gmm)</summary>

<br/>

- [x]  公用数据库
- [x]  转移models至pymysql

</br>
</details>

## Database

```
'HOST': 'rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com',
'NAME': 'spoc',
'USER': 'root',
'PASSWORD': 'myja&*$4X579cKr',
'PORT': '3306'
```

### Entity

```
teacher(id, name, password, sex, department, telephone, email)

student(id, name, password, sex, department, orientation)

admin(id, password, telephone, email)

course(id, name, department, volume, credit)

material(id, department, obtain)

group(id, orientation, department, volume)
```

### Relation

```
courseEvaluation(id, content) //anonymity //

courseSelection(student_id, course_id)

groupJoin(student_id, group_id)

studentMaterialObtain(student_id, material_id)

groupMaterialObtain(group_id, material_id)

courseCreate(course_id, teacher_id, time)

groupTutor(course_id, teacher_id) //no time

grade() //打分
```

## Team

[@fangzhou0216](https://github.com/fangzhou0216), [@Mike-Smith-rem](https://github.com/Mike-Smith-rem), [@imingx](https://github.com/imingx).

## License



