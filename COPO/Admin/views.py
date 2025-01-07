import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.db import models
from django.urls import reverse
import time

from Teachers.models import Students,Branch,Batch,Teacher
from Admin.models import AdminUSERS, SubjectDB, CONAMES, Corelationdata, COPOAcheiveddata
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
            print("Data received: ", data_dict)
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
                    data = {"redirect_url": "/Admin/Home/RenderUpdateCO/"}
                    return JsonResponse(data)

            except CONAMES.DoesNotExist:
                if data:
                    data_dict = json.loads(data)  # Convert JSON string to a dictionary
                    print("Data received:", data_dict)
                    sinstance = get_object_or_404(SubjectDB, subject=sub)
                    ins = CONAMES.objects.create(subject=sinstance, data=data_dict)
                    ins.save()
                    messages.success(request, 'Saved Successfully ')
                    data = {"redirect_url": "/Admin/Home/RenderUpdateCO/"}
                    return JsonResponse(data)


def retrieveco(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            sub= request.POST['sub']
            values = SubjectDB.objects.get(subject = sub)
            try:
                Comatri = Corelationdata.objects.get(subject = sub)

                data = {'subject':sub,'subid':values.subject_id,'sempom':
                    values.Sem_th_pom,'NOCO':values.NOCO,'NOPO':values.NOPO,'NOPSO':values.NOPSO,
                    'Cos':values.CONAMES,'COMatrix':Comatri.data}
                return JsonResponse(data)
            except Corelationdata.DoesNotExist:
                data = {'subject': sub, 'subid': values.subject_id, 'sempom':
                    values.Sem_th_pom, 'NOCO': values.NOCO, 'NOPO': values.NOPO, 'NOPSO': values.NOPSO,
                        'Cos': values.CONAMES}

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

def saveCOrelMatrix(request):
    if 'user_id' in request.session:

        if request.method == 'POST':
            sub = request.POST['sub']
            subinst = SubjectDB.objects.get(subject = sub)
            data = request.POST['matrix']
            if data :
                data_dict = json.loads(data)
                try:
                    retinst = Corelationdata.objects.get(subject = sub)
                    retinst.data=data_dict
                    retinst.save()
                    return JsonResponse({'message':'Data Saved Successfully'})
                except Corelationdata.DoesNotExist:
                    inst = Corelationdata.objects.create(subject=subinst, data=data_dict)
                    inst.save()
                    return JsonResponse({'message':'Data Created Successfully'})

                    retinst.data = data_dict
                    retinst.save()
                    return JsonResponse({'message':'Error Data Not Updated'})

def ResetPass(request):
    if request.method == 'POST':
        em = request.POST['Email']
        fname = request.POST['fname']
        try:
            aus = AdminUSERS.objects.get(email=em,fname=fname)


            return HttpResponse("""
            <!DOCTYPE html>

            <html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    
    
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.1/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
    body{
    background-color:darkslategrey;}
        .fade-out {
            opacity: 0;
            transition: opacity 0.5s ease-out;
        }
    </style>
</head>""" f"""<body >
                 <div class="modal fade show" id="ForgetPass" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-modal="true" role="dialog" style="display:block;">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Password</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                     
                        
                        <div class="mb-3"><label for="password">Password is :</label>
                            <input class=" form-control" id="password" value= "{ aus.password }">
                        </div>

                </div>

                 
                 
            </div>
        </div>
    </div>
""" """
    <script>
            window.onload = function () {
                setTimeout(() => {
                    alert('Please Copy the Password, you will be redirected to login page in 5 seconds')
                    setTimeout(()=>{
                    window.location = '/Login/loginpage/'},3000)
                    
                }, 1000);
            }
        </script><script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.1/js/bootstrap.bundle.min.js"></script>
</body></html>
""")

        except AdminUSERS.DoesNotExist:
            return HttpResponse("""
            <!DOCTYPE html>

            <html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>

    <link rel="stylesheet" href="{% static '/styles.css' %}">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="{% static 'script.js' %}"></script>
    <style>
        .fade-out {
            opacity: 0;
            transition: opacity 0.5s ease-out;
        }
    </style>
</head>
<body style="background-color:darkslategrey;">
                                 <div class="modal fade" id="ForgetPass" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
                        aria-labelledby="staticBackdropLabel" aria-modal="true">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Password</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <script>
                            window.onload = function () {
                setTimeout(() => {
                    alert('Wrong Credentials Please Try again .')
                    setTimeout(()=>{
                    window.location = '/Login/loginpage/'},1000)
                    
                }, 500);
            }
                        </script>
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.1/js/bootstrap.bundle.min.js"></script>
</body></html>
                """)

def SaveCOPOAchieved(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            copoAchDa = request.POST['table1']
            copoAchExDa = request.POST['table2']
            coursExdata = request.POST['table3']
            coursExAchdata = request.POST['table4']

            teacherUName = request.POST['teacher']
            sub = request.POST['sub']

            copo = json.loads(copoAchDa)
            copoExdata = json.loads(copoAchExDa)
            courseExitAch = json.loads(coursExdata)
            courseExitExAch = json.loads(coursExAchdata)
            print(copo)
            print(copoExdata)
            print(courseExitAch)
            print(courseExitExAch)

            subinst = SubjectDB.objects.get(subject = sub)
            teacinst =AdminUSERS.objects.get(username = teacherUName,email = request.session['user_id'])
            uploaded_by = teacinst
            print(uploaded_by)
            inst = COPOAcheiveddata.objects.create(subject = subinst, copoAch=copo,copoAchExt=copoExdata
                                                   ,CourseCopoAch=courseExitAch,CourseCopoAchExt=courseExitExAch,
                                                   uploaded_by=uploaded_by)
            inst.save()
            return JsonResponse({})

def renderCONFBB(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            return render(request,'Admin/addremoveBatchBranch.html')
def renderaddBr(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            return render(request,'Admin/addBranch.html')
def renderremBr(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            br=Branch.objects.all()
            param = {'br':br}
            return render(request,'Admin/removeBranch.html',param)
def renderaddBa(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            return render(request,'Admin/addBatch.html')
def renderremBa(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            ba = Batch.objects.all()
            param = {'ba':ba}
            return render(request,'Admin/removeBatch.html',param)

def renderaddBrf(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            br = request.POST['name']
            try:
                brinst = Branch.objects.get(branch =br)
                messages.success(request, 'Branch Already Exists')
                return redirect("HomePage")
            except Branch.DoesNotExist:
                brinst = Branch.objects.create(branch = br)
                brinst.save()
                messages.success(request,'Branch Added Successfully')
                return redirect("HomePage")

def renderremBrf(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            br = request.POST['name']
            try:
                brinst = Branch.objects.get(branch =br)
                Branch.objects.get(branch=br).delete()
                messages.success(request, 'Branch Removed Successfully ')
                return redirect("HomePage")

            except Branch.DoesNotExist:
                messages.success(request,'Branch Doesnt Exists ')
                return redirect("HomePage")


def renderaddBaf(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            ey = request.POST['entry_year']
            fy = request.POST['final_year']
            strin = str(ey) + '-' + str(fy)
            print(str)
            try:
                bainst = Batch.objects.get(batch=strin)
                messages.success(request, 'Batch Already Exists')
                return redirect("HomePage")

            except Batch.DoesNotExist:
                bainst = Batch.objects.create(batch=strin)
                bainst.save()
                messages.success(request, 'Batch Added Successfully')
                return redirect("HomePage")


def renderremBaf(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            ey = request.POST['entry_year']
            fy = request.POST['final_year']
            strin = str(ey) + '-' + str(fy)
            print(str)
            try:
                bainst =Batch.objects.get(batch=strin)
                Batch.objects.get(batch=strin).delete()
                messages.success(request, 'Batch Removed Successfully ')
                return redirect("HomePage")
            except Batch.DoesNotExist:
                messages.success(request, 'Batch Doesnt Exist ')
                return redirect("HomePage")

def ConsolidatedCorelations(request):
    if 'user_id' in request.session:
        if request.method == 'GET':
            inst = Corelationdata.objects.all()
            subinst = SubjectDB.objects.all()
            param = {'data':zip(inst,subinst)}
            return render(request,'Admin/ViewSheets Together.html',param)


