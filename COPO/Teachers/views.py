from click.core import batch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from Teachers.models import Teacher, Students, Branch, Batch


# Create your views here.
def index(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username = name)
            branches = Branch.objects.all()
            batch =Batch.objects.all()
            params = {'teachname':name,'subject':teacher.subject,'branch':branches,'batch':batch}
            return render(request,'Teachers/TeachersHome.html',params)
        else:
            messages.ERROR(request,"You are not Logged In")
            return redirect("LogInPage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetch(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username=name)
            qno = teacher.subques
            br = request.POST.get('branch','')
            ba = request.POST.get('batch','')
        students = Students.objects.filter(branch = br,batch = ba )
        branches = Branch.objects.all()
        batch = Batch.objects.all()
        params = {'Students':students,'NoofQuestions':range(1,qno+1),'teachname':name,'subject':teacher.subject,'branch':branches,'batch':batch}
        return render(request,'Teachers/TeachersHome.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetchadmin(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username=name)
            qno = teacher.subques
            br = request.POST.get('branch','')
            ba = request.POST.get('batch','')
        students = Students.objects.filter(branch = br,batch = ba )
        branches = Branch.objects.all()
        batch = Batch.objects.all()
        params = {'Students':students,'NoofQuestions':range(1,qno+1),'teachname':name,'subject':teacher.subject,'branch':branches,'batch':batch}
        return render(request,'Teachers/TeachersHomeswitch.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})


def adminhome(request):
    if 'user_id' in request.session:

        user_id = request.session.get('user_id')
        if user_id:
            name = request.session['username']
            teacher = Teacher.objects.get(Username=name)
            branches = Branch.objects.all()
            batch = Batch.objects.all()
            params = {'teachname': name, 'subject': teacher.subject, 'branch': branches, 'batch': batch}
            return render(request, 'Teachers/TeachersHomeswitch.html', params)
        else:
            messages.ERROR(request, "You are not Logged In")
            return redirect("LogInPage")
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})

def fetchteacherform(request):
    if 'user_id' in request.session:

        teacher =Teacher.objects.all()

        params = {'teacher':teacher}
        return render(request,'Admin/ConsolidatedThreshold.html',params)
    return render(request, 'Login/login.html', {'message': "No session found. Please log in."})



