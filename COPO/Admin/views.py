import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.db import models
from django.urls import reverse
import time

from Teachers.models import Students,Branch,Batch,Teacher
from Admin.models import AdminUSERS, SubjectDB, CONAMES
from Teachers.models import Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8



# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return render(request,'Admin/homepage.html')
    else:
        return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def adduserfunction(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            Uname   = request.POST['username']
            email   = request.POST['email']
            fname   = request.POST['fname']
            lname   = request.POST['lname']
            sem     = request.POST['Sem']
            passw   = request.POST['password']
            utype   = request.POST['usertype']
            sub     = request.POST['subject']


            user = AdminUSERS.objects.filter(email = email).first()

            if not user :
                newuser = AdminUSERS.objects.create(sem = sem,email = email,usertype=utype ,password=passw ,fname= fname ,lname=lname ,username=Uname)
                newuser.save()
                newuser.refresh_from_db()
                # time.sleep(0.3)
                admin_user = AdminUSERS.objects.filter(email=email).first()

                if admin_user:
                    tea = Teacher.objects.filter(email=admin_user).first() # Match using the foreign key
                    su =SubjectDB.objects.get(subject = sub)
                    if tea:
                        tea.subject = sub
                        tea.Username = Uname
                        tea.subject_id =su.subject_id
                        tea.save()
                    else:
                        # If no Teacher exists, create a new one
                        Teacher.objects.create(email=admin_user, subject=sub, Username=Uname)
                else:
                    messages.error(request, 'User not found in AdminUSERS')
                messages.success(request, 'Successfully added User')
            else:
                messages.error(request, 'User Already Exists')
            return redirect("HomePage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fillTeachers(demail,dname,dsub,dques):
    tea = Teacher.objects.create(email=demail, username=dname, subject=dsub, subques=dques)
    tea.save()

def adduserform(request):
    if 'user_id' in request.session:
        s1 = list(Sem1.objects.all())
        s2 = list(Sem2.objects.all())
        s3 = list(Sem3.objects.all())
        s4 = list(Sem4.objects.all())
        s5 = list(Sem5.objects.all())
        s6 = list(Sem6.objects.all())
        s7 = list(Sem7.objects.all())
        s8 = list(Sem8.objects.all())

        s = s1+s2+s3+s4+s5+s6+s7+s8
        params = {'Subjects':s}
        return render(request, 'Admin/addteachersform.html',params)
    messages.success(request, "No session found. Please log in.")
    return render(request, 'Login/login.html', )

def removeuserform(request):
    if 'user_id' in request.session:
        users=AdminUSERS.objects.values_list('username',flat=True)
        params = {'Allusers':users}
        return render(request,'Admin/Removeteach.html',params)
    messages.success(request, "No session found. Please log in.")
    return render(request, 'Login/login.html', )

def removeuserfunction(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            rem = request.POST.get('remuser','')
            AdminUSERS.objects.filter(username = rem).delete()
            messages.success(request,'Successfully removed the user')
            return redirect("HomePage")
    messages.success(request, "No session found. Please log in.")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def addstudent(request):
    if 'user_id' in request.session:
        return render(request,'Admin/addstudentsform.html')
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def addstudentfunc(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            name = request.POST['name']
            prn = request.POST['prn']
            branch = request.POST['branch']
            batch = request.POST['batch']
            stue = Students.objects.filter(prn = prn).first()
            if not stue:
                student = Students(name=name,prn=prn,branch=branch,batch=batch)
                student.save()
                messages.success(request,'Added Student Successfully')
                return redirect("HomePage")
            else:
                messages.error(request,'Student Already Exists')

    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def addstudentBW(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            jsonvalue = request.POST.get('data')
            data_dict =json.loads(jsonvalue)
            try:
                branch = Branch.objects.get(branch = data_dict['branch'])
            except Branch.DoesNotExist:
                return JsonResponse({'message':'Branch DNE,Create a Branch' })
            try:
                batch = Batch.objects.get(batch = data_dict['batch'])
            except Batch.DoesNotExist:
                return JsonResponse({'message':'Batch DNE Create Batch'})

            print("Data received: ",data_dict)
            for x,y in zip(data_dict['prn'],data_dict['name']):
                try:
                    prn_inst = Students.objects.get(prn = x)

                except Students.DoesNotExist:
                    new = Students.objects.create(name = y,prn = x,branch =branch,batch = batch )
                    new.save()
            return JsonResponse({'message':'Successfully saved the data'})


def removestudentfunc(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            rem = request.POST['Student']
            print(rem)
            Students.objects.get( name=rem).delete()
            messages.success(request, 'Successfully removed the user')
            return redirect("HomePage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})



def removestudent(request):
    if 'user_id' in request.session:
        br = Branch.objects.all()
        ba = Batch.objects.all()
        params = {'branch':br,'batch':ba}
        return render(request, 'Admin/removestudent.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetchstudent(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            br = request.POST.get('branch', '')
            ba = request.POST.get('batch', '')
            students = Students.objects.filter(branch=br, batch=ba)

            if not students :
                messages.error(request,'No Students found')
                return redirect("HomePage")
            else :
                params = {'Student':students}
                return render(request, 'Admin/removestudent.html', params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def returnsSubforSem(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            sem =request.POST.get('sem')

            if not sem:
                # Handle missing 'Sem' parameter
                return JsonResponse({'error': 'Missing "Sem" parameter'}, status=400)
            subs = SubjectDB.objects.filter(sem=sem)
            sub = list(subs.values('subject'))
            data = {'subs':sub}
            print(sub)
            return JsonResponse(data)

def RenderSubjectHtml(request):
    if 'user_id' in request.session:
        return render(request,'Admin/ConfigureSubjects.html')

def ConfigureAndEditSubject(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            sub = request.POST['subject']
            iath1 = request.POST['iath1']
            iath2 = request.POST['iath2']
            iath3 = request.POST['iath3']
            iathpom = request.POST['iathpom']
            semthpom = request.POST['semthpom']
            NoCO = request.POST['NOCO']
            NoPO = request.POST['NOPO']
            NoPSO = request.POST['NOPSO']
            NOQues = request.POST['ques']

            obj = SubjectDB.objects.get(subject = sub)
            obj.ia_th_lvl1_sc = iath1
            obj.ia_th_lvl2_sc = iath2
            obj.ia_th_lvl3_sc = iath3
            obj.ia_th_pom = iathpom
            obj.Sem_th_pom = semthpom
            obj.NOCO = NoCO
            obj.NOPO = NoPO
            obj.NOPSO = NoPSO
            obj.subques = NOQues
            obj.save()
            messages.success(request, 'Successfully Configured the Subject')
            return render(request,'Admin/Configure COS.html')

def UpdateCOS(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            sub = request.POST.get('subject')

            if not sub:
                # Handle missing 'Sem' parameter
                return JsonResponse({'error': 'Missing "Sem" parameter'}, status=400)
            subs = SubjectDB.objects.get(subject = sub)
            data = {'cos':subs.NOCO }
            return JsonResponse( data)
def renderConfigureCos(request):
    if 'user_id' in request.session:
        return render(request,'Admin/Configure COS.html')

def saveCOs(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            sub = request.POST['subject']
            data = request.POST.get('data')
            try:
                sub_ins= CONAMES.objects.get(subject=sub)
                if data:
                    data_dict = json.loads(data)  # Convert JSON string to a dictionary
                    print("Data received:", data_dict)
                    sub_ins.data = data_dict
                    sub_ins.save()
                    messages.success(request, 'Edited Successfully ')
                    data = {"redirect_url": "/Admin/Home/adduserform/RenderUpdateCO/"}
                    return JsonResponse(data)

            except CONAMES.DoesNotExist:
                if data:
                    data_dict = json.loads(data)  # Convert JSON string to a dictionary
                    print("Data received:", data_dict)
                    sinstance = get_object_or_404(SubjectDB, subject=sub)
                    ins = CONAMES.objects.create(subject=sinstance, data=data_dict)
                    ins.save()
                    messages.success(request, 'Saved Successfully ')
                    data = {"redirect_url": "/Admin/Home/adduserform/RenderUpdateCO/"}
                    return JsonResponse(data)
def returnBranchBatch(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            batch = Batch.objects.all();
            branch = Branch.objects.all();

            BatchL = list(batch.values('batch'))
            BranchL = list(branch.values('branch'))
            data = {'batch':BatchL,'branch':BranchL }

            return JsonResponse(data)


