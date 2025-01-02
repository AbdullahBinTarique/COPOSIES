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
    path('Home/SaveCOmatrix/', views.saveCOMatrix, name="SaveCoMatrix"),

    path('Home/Student/fetch/', views.fetchstudent, name="FetchStudent"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),
    path('Home/retrieveco/', views.retrieveco, name="COendpoint"),

    # path('Home/Teachers/<slug:slug>',views.slugusers,name="Sluguser")


    path('Home/adduserform/AskSem/',views.returnsSubforSem,name = "EndpointSem"),
    path('Home/RenderUpdateCO/', views.renderConfigureCos, name="COS"),

    path('Home/UpdateCO/', views.UpdateCOS, name="EndpointCOS"),
    path('Home/SaveCOS/', views.saveCOs, name="SaveCO"),

    path('Home/viewBranchBatchEndpt/',views.returnBranchBatch,name="BranchBatchEndPt"),

    path('Home/SaveCOPOAcheived/',views.SaveCOPOAchieved,name="SaveCOAcheived"),

    path('Home/RenderConfBB',views.renderCONFBB,name="ConfBB"),
    path('Home/RenderConfBB/addBranch', views.renderaddBr, name="AddBr"),
    path('Home/RenderConfBB/remBranch', views.renderremBr, name="RemBr"),
    path('Home/RenderConfBB/addBatch', views.renderaddBa, name="AddBa"),
    path('Home/RenderConfBB/remBatch', views.renderremBa, name="RemBa"),

path('Home/RenderConfBB/addBranchfunc', views.renderaddBrf, name="AddBrf"),
    path('Home/RenderConfBB/remBranchfunc', views.renderremBrf, name="RemBrf"),
    path('Home/RenderConfBB/addBatchfunc', views.renderaddBaf, name="AddBaf"),
    path('Home/RenderConfBB/remBatchfunc', views.renderremBaf, name="RemBaf"),

    # path('ConsolidatedCoAttainment/',views.ccoattainment,name="HomePage"),

    # path('ConsolidatedCourseOutcome/',views.ccourseoutcome,name="HomePage"),



]