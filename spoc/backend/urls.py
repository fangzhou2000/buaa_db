from django.urls import path
from . import views

urlpatterns = [
    path('DataTest/', views.DataTest.as_view()),
]