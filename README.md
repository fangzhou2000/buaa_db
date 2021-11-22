#  BUAA DB

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

## DataBase

```
'HOST': 'rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com',
'NAME': 'spoc',
'USER': 'root',
'PASSWORD': 'myja&*$4X579cKr',
'PORT': '3306'
```

## DataBase Design

### Final Design

**Entity：**

|                 Entity                  | Key  | Description |
| :-------------------------------------: | :--: | :---------: |
|      `student(id, password, name)`      | `id` |  学生信息   |
|      `teacher(id, password, name)`      | `id` |  教师信息   |
|          `material(id, name)`           | `id` |  学习材料   |
|           `course(id, name)`            | `id` |  课程信息   |
| `comment(id, course_id, content, time)` | `id` |    评论     |
|  `posttheme(id, title, content, time)`  | `id` |   主题帖    |
| `post(id, posttheme_id, content, time)` | `id` |    跟帖     |

**Relation：**

|                   Relation                    |    Key    |  Description   |
| :-------------------------------------------: | :-------: | :------------: |
|    `student_course(student_id, course_id)`    | `all-key` |    学生选课    |
|    `teacher_course(teacher_id, course_id)`    | `all-key` |    教师开课    |
|  `teacher_material(teacher_id, material_id)`  | `all-key` |  教师提供材料  |
|   `course_material(course_id, material_id)`   | `all-key` |  课程对应材料  |
|   `student_comment(student_id, comment_id)`   | `all-key` |  学生发表评论  |
| `student_posttheme(student_id, posttheme_id)` | `all-key` | 学生发表主题帖 |
|      `student_post(student_id, post_id)`      | `all-key` |    学生跟帖    |

### E-R Diagram

![](./img/1122_er.svg)



![er](./img/1122_er_full.svg)

<img src="./img/1122_db.svg" alt="1122_db" style="zoom: 33%;" />

### Plan Design

```
Entity

teacher(id, name, password, sex, department, telephone, email)
student(id, name, password, sex, department, orientation)
admin(id, password, telephone, email)
course(id, name, department, volume, credit)
material(id, name, department, obtain)
group(id, orientation, department, volume)

Relation

courseEvaluation(id, content)
courseSelection(student_id, course_id)
groupJoin(student_id, group_id)
studentMaterialObtain(student_id, material_id)
groupMaterialObtain(group_id, material_id)
courseCreate(course_id, teacher_id, time)
groupTutor(course_id, teacher_id) //no time
grade() //打分
```

## Team

[@fangzhou0216][tqj], [@Mike-Smith-rem][oyk], [@imingx][gmm].

## License




[tqj]: https://github.com/fangzhou0216
[oyk]: https://github.com/Mike-Smith-rem
[gmm]: https://github.com/imingx