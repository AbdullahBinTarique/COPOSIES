import json

from click.core import batch
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from Admin.models import SubjectDB, CONAMES, AdminUSERS
from Teachers.models import Teacher, Students, Branch, Batch



def fetch(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']

            TN = AdminUSERS.objects.get(username = name)

            suba = request.POST['subjectDL']

            sub = SubjectDB.objects.get(subject=suba)
            qno = sub.subques
            br = request.POST.get('branch', '')
            ba = request.POST.get('batch', '')
            suball = SubjectDB.objects.all()
            students = Students.objects.filter(branch=br, batch=ba)
            branches = Branch.objects.all()
            batch = Batch.objects.all()
            params = {'Students': students, 'NoofQuestions': range(1, qno + 1), 'teachname': name,'TN':TN.slug,
                  'subject': sub.subject, 'branch': branches, 'qno': qno,'sub':suball,'suba':suba,
                  'batch': batch, 'lvl1Threshold': sub.ia_th_lvl1_sc, 'lvl2Threshold': sub.ia_th_lvl2_sc,
                  'lvl3Threshold': sub.ia_th_lvl3_sc
            , 'ia_th_pom': sub.ia_th_pom,'Batch':ba,'Branch':br
                  }
            return render(request,'Teachers/TeachersHome.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetchadmin(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            suba = request.POST['subjectDL']
            TN = AdminUSERS.objects.get(username=name)
            sub= SubjectDB.objects.get(subject =suba )
            qno = sub.subques
            br = request.POST.get('branch','')
            ba = request.POST.get('batch','')
            suball = SubjectDB.objects.all()
        try:
            students = Students.objects.filter(branch = br,batch = ba )
            branches = Branch.objects.all()
            batch = Batch.objects.all()
            params = {'Students': students, 'NoofQuestions': range(1, qno + 1), 'teachname': name, 'TN': TN.slug,
                      'subject': sub.subject, 'branch': branches, 'qno': qno,
                      'batch': batch, 'lvl1Threshold': sub.ia_th_lvl1_sc, 'lvl2Threshold': sub.ia_th_lvl2_sc,
                      'lvl3Threshold': sub.ia_th_lvl3_sc,'sub':suball,'suba':suba
                , 'ia_th_pom': sub.ia_th_pom, 'Batch': ba, 'Branch': br
                      }
            return render(request, 'Teachers/TeachersHomeswitch.html', params)

        except Students.DoesNotExist:
            messages.success(request,'Students Does Not Exists')
            return render(request, 'Teachers/TeachersHomeswitch.html', params)





    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})


def adminhome(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username=name)
            TN = AdminUSERS.objects.get(username=name)
            branches = Branch.objects.all()
            batch = Batch.objects.all()
            sub = SubjectDB.objects.all()
            params = {'teachname': name,'sub':sub,'TN':TN.slug,'subject': teacher.subject, 'branch': branches, 'batch': batch}
            return render(request, 'Teachers/TeachersHomeswitch.html', params)
        else:
            messages.ERROR(request, "You are not Logged In")
            return redirect("LogInPage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def teahome(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username=name)
            TN = AdminUSERS.objects.get(username=name)
            branches = Branch.objects.all()
            batch = Batch.objects.all()
            sub = SubjectDB.objects.all()
            params = {'teachname': name,'sub':sub,'TN':TN.slug,'subject': teacher.subject, 'branch': branches, 'batch': batch}
            return render(request, 'Teachers/TeachersHome.html', params)
        else:
            messages.ERROR(request, "You are not Logged In")
            return redirect("LogInPage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetchteacherform(request):
    if 'user_id' in request.session:

        teacher =SubjectDB.objects.all()


        params = {'teacher':teacher}
        return render(request,'Admin/ConsolidatedThreshold.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})




