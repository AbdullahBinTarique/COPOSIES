from django.urls import path
from . import views

urlpatterns = [

    path('loginpage/', views.index, name = "LogInPage"),
    # path('login/',views.handlelogin,name = "LogIn"),
    path('login/',views.handleloginuser,name = "LogIn"),

    path('logout/',views.handlelogoutuser,name = "Logout"),
    # path('signin/',views.signin,name = "SignIn"),
]