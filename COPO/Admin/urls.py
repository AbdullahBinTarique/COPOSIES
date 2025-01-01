from django.urls import path,include
from . import views


urlpatterns = [
    path('Home/', views.index, name="HomePage"),
    path('Home/adduserform/',views.adduserform,name="AddUserForm"),
    path('Home/adduserform/adduserfunction/', views.adduserfunction, name="AddUserFunction"),
    path('Home/ConfSubjects/', views.RenderSubjectHtml, name="ConfigureSubjectsHtml"),
    path('Home/DataSubjects/', views.ConfigureAndEditSubject, name="ConfigureSubjectsHtml"),

    path('Home/removeuser/',views.removeuserform,name="RemoveUser"),
    path('Home/removeuser/func', views.removeuserfunction, name="RemoveUserfunc"),

    path('Home/addstudent/',views.addstudent,name="AddStudent"),
    path('Home/addstudentBW/', views.addstudentBW, name="AddStudentBatchW"),

    path('Home/addstudent/addstudentfunction/', views.addstudentfunc, name="AddStudentfunc"),

    path('Home/removestudent/',views.removestudent,name="RemoveStudent"),
    path('Home/Student/fetch/', views.fetchstudent, name="FetchStudent"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),
    # path('Home/Teachers/<slug:slug>',views.slugusers,name="Sluguser")


    path('Home/adduserform/AskSem/',views.returnsSubforSem,name = "EndpointSem"),
    path('Home/adduserform/RenderUpdateCO/', views.renderConfigureCos, name="COS"),

    path('Home/adduserform/UpdateCO/', views.UpdateCOS, name="EndpointCOS"),
    path('Home/adduserform/SaveCOS/', views.saveCOs, name="SaveCO"),

    path('Home/viewBranchBatchEndpt/',views.returnBranchBatch,name="BranchBatchEndPt"),

    # path('ConsolidateIndirectAttainment/',views.cindirattainment,name="HomePage"),

    # path('ConsolidatedThresholdSettings/',views.cthreshsettings,name="HomePage"),

    # path('ConsolidatedCoAttainment/',views.ccoattainment,name="HomePage"),

    # path('ConsolidatedCourseOutcome/',views.ccourseoutcome,name="HomePage"),



]