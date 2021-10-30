from django.urls import path
from . import views

urlpatterns = [
    path('StudentLogin/', views.StudentLogin.as_view()),
    path('StudentRegister/', views.StudentRegister.as_view()),
    path('TeacherLogin/', views.TeacherLogin.as_view()),
    path('TeacherRegister/', views.TeacherRegister.as_view()),
    path('GetCourseList/', views.GetCourseList.as_view()),
    path('SelectCourse/', views.SelectCourse.as_view()),
    path('StudentChange/', views.StudentChange.as_view()),
    path('TeacherChange/', views.TeacherChange.as_view()),
    path('GetStudentCourseList/', views.GetStudentCourseList.as_view()),
    path('DropCourse/', views.DropCourse.as_view()),
    path('GetTeacherCourseList/', views.GetTeacherCourseList.as_view()),
    path('BuildCourse/', views.BuildCourse.as_view()),
    path('ChangeCourse/', views.ChangeCourse.as_view()),
    path('CancelCourse/', views.CancelCourse.as_view()),
    path('GetCourseInfo/', views.GetCourseInfo.as_view()),
    path('GetMaterialList/', views.GetMaterialList.as_view()),
]