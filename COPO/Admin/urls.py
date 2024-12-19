from django.urls import path,include
from . import views


urlpatterns = [
    path('Home/', views.index, name="HomePage"),
    path('Home/adduserform/',views.adduserform,name="AddUserForm"),
    path('Home/adduserform/adduserfunction/', views.adduserfunction, name="AddUserFunction"),
    path('Home/removeuser/',views.removeuserform,name="RemoveUser"),
    path('Home/removeuser/func', views.removeuserfunction, name="RemoveUserfunc"),

    path('Home/addstudent/',views.addstudent,name="AddStudent"),
    path('Home/addstudent/addstudentfunction/', views.addstudentfunc, name="AddStudentfunc"),

    path('Home/removestudent/',views.removestudent,name="RemoveStudent"),
    path('Home/Student/fetch/', views.fetchstudent, name="FetchStudent"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),
    # path('Home/Teachers/<slug:slug>',views.slugusers,name="Sluguser")


    # path('ConsolidateCorrelationMatrix/',views.ccorrmatrix,name="HomePage"),

    # path('ConsolidateDirectAttainment/',views.cdirattainment,name="HomePage"),

    # path('ConsolidateIndirectAttainment/',views.cindirattainment,name="HomePage"),

    # path('ConsolidatedThresholdSettings/',views.cthreshsettings,name="HomePage"),

    # path('ConsolidatedCoAttainment/',views.ccoattainment,name="HomePage"),

    # path('ConsolidatedCourseOutcome/',views.ccourseoutcome,name="HomePage"),



]