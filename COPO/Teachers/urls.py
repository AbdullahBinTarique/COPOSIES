from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.index,name="TeachersHome"),
    path('admins/', views.adminhome  , name="AdminTeachersHome"),

    path('fetch/',views.fetch,name="FetchStudents"),
    path('fetchteacherform/',views.fetchteacherform ,name="Fetchtf"),
    path('fetchadmin/', views.fetchadmin, name="FetchAdminStudents"),

]