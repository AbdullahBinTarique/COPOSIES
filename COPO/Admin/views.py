from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.db import models
from Teachers.models import Students,Branch,Batch,Teacher
from Admin.models import AdminUSERS
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
            sem     = request.POST['sem']
            passw   = request.POST['password']
            utype   = request.POST['usertype']
            sub     = request.POST['subject']
            ques    =request.POST['ques']

            user = AdminUSERS.objects.filter(email = email).first()

            if not user :
                newuser = AdminUSERS.objects.create(sem = sem,email = email,usertype=utype ,password=passw ,fname= fname ,lname=lname ,username=Uname)
                newuser.save()

                tea = Teacher.objects.filter(email = email).first()
                tea.subject = sub
                tea.subques = ques
                tea.Username =Uname
                tea.save()
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
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def removeuserform(request):
    if 'user_id' in request.session:
        users=AdminUSERS.objects.values_list('username',flat=True)
        params = {'Allusers':users}
        return render(request,'Admin/Removeteach.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def removeuserfunction(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            rem = request.POST.get('remuser','')
            AdminUSERS.objects.filter(username = rem).delete()
            messages.success(request,'Successfully removed the user')
            return redirect("HomePage")
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


def removestudentfunc(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            rem = request.POST.get('remuser', '')
            Students.objects.filter( name=rem).delete()
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

