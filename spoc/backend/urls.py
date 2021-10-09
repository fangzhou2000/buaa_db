from django.urls import path
from . import views

urlpatterns = [
    path('StudentLogin/', views.StudentLogin.as_view()),
    path('StudentRegister/', views.StudentRegister.as_view()),
    path('TeacherLogin/', views.TeacherLogin.as_view()),
    path('GetCourseList/', views.GetCourseList.as_view()),
    path('SelectCourse/', views.SelectCourse.as_view()),
    path('StudentChange/', views.StudentChange.as_view()),
    path('TeacherChange/', views.TeacherChange.as_view()),
    path('GetMyCourseList/', views.GetMyCourseList.as_view())
]