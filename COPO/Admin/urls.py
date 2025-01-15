from django.urls import path,include
from . import views


urlpatterns = [
    path('Home/', views.index, name="HomePage"),
    path('Home/adduserform/',views.adduserform,name="AddUserForm"),
    path('Home/adduserform/adduserfunction/', views.adduserfunction, name="AddUserFunction"),
    path('Home/ConfSubjects/', views.RenderSubjectHtml, name="ConfigureSubjectsHtml"),
    path('Home/DataSubjects/', views.ConfigureAndEditSubject, name="ConfigureSubjects"),

    path('Home/removeuser/',views.removeuserform,name="RemoveUser"),
    path('Home/removeuser/func', views.removeuserfunction, name="RemoveUserfunc"),

    path('Home/addstudent/',views.addstudent,name="AddStudent"),
    path('Home/addstudentBW/', views.addstudentBW, name="AddStudentBatchW"),

    path('Home/addstudent/addstudentfunction/', views.addstudentfunc, name="AddStudentfunc"),

    path('Home/removestudent/',views.removestudent,name="RemoveStudent"),
    path('Home/SaveCOmatrix/', views.saveCOrelMatrix, name="SaveCorelMatrix"),

    path('Home/Student/fetch/', views.fetchstudent, name="FetchStudent"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),

    path('Home/removestudent/func/', views.removestudentfunc, name="RemoveStudentfunc"),
    path('Home/retrieveco/', views.retrieveco, name="COendpoint"),

    # path('Home/Teachers/<slug:slug>',views.slugusers,name="Sluguser")


    path('Home/adduserform/AskSem/',views.returnsSubforSem,name = "EndpointSem"),
    path('Home/RenderUpdateCO/', views.renderConfigureCos, name="COS"),

    path('Home/UpdateCO/', views.UpdateCOS, name="EndpointCOS"),
    path('Home/SaveCOS/', views.saveCOs, name="SaveCO"),
    path('Home/resetPass/', views.ResetPass, name="ResetPass"),

    path('Home/viewBranchBatchEndpt/',views.returnBranchBatch,name="BranchBatchEndPt"),

    path('Home/SaveCOPOAcheived/',views.SaveCOPOAchieved,name="SaveCOAcheived"),

    path('Home/RenderConfBB',views.renderCONFBB,name="ConfBB"),
    path('Home/RenderConfBB/addBranch', views.renderaddBr, name="AddBr"),
    path('Home/RenderConfBB/remBranch', views.renderremBr, name="RemBr"),
    path('Home/RenderConfBB/addBatch', views.renderaddBa, name="AddBa"),
    path('Home/RenderConfBB/remBatch', views.renderremBa, name="RemBa"),

path('Home/RenderConfBB/addBranchfunc', views.renderaddBrf, name="AddBrf"),
    path('Home/RenderConfBB/remBranchfunc', views.renderremBrf, name="RemBrf"),
    path('Home/RenderConfBB/remSubjfunc', views.renderremsubf, name="RemSubf"),
    path('Home/RenderConfBB/addSubjfunc', views.renderaddsubf, name="AddSubf"),
    path('Home/RenderConfBB/remSubj', views.renderremsub, name="RemSub"),
    path('Home/RenderConfBB/addSubj', views.renderaddsub, name="AddSub"),

    path('Home/RenderConfBB/addBatchfunc', views.renderaddBaf, name="AddBaf"),
    path('Home/RenderConfBB/remBatchfunc', views.renderremBaf, name="RemBaf"),

    path('Home/ViewConsolidateCorelations',views.ConsolidatedCorelations,name="CCorelations"),
    path('Home/ViewCOPOAchieved/', views.ConsolidatedAcheived, name="COPOAchieved"),
path('Home/ViewCONAMES/', views.viewCONSconames, name="COPONAMES"),
path('Home/ViewAVGCOPO/', views.viewAVGCOPO, name="AVGCOPO"),
path('Home/renderAVGCOPO/', views.avgcopo, name="RenderAVGCOPO"),
    path('Home/ViewCourseExitCOPOAchieved/', views.ConsolidatedCourseExitCOPO, name="CourseExitCOPOAchieved"),
    path('Home/ViewCourseExitThresholdBasedCOPOAchieved/', views.CourseExitThresholdBased, name="CourseExitThresholdBasesCOPOAchieved"),

    path('Home/ViewExternalCOPOAchieved/', views.ConsolidatedThresholdbasedScaledAcheived, name="ExternalCOPOAchieved"),

    # path('Home/deleteEntry/', views.deleteEntry, name="deleteEntry"),
    # view avg copoThreshscaled
    # view avg copoexit
    # view avg copothreshbasedexit

    # path('ConsolidatedCourseOutcome/',views.ccourseoutcome,name="HomePage"),



]