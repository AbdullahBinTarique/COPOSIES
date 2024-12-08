
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from Admin.models import AdminUSERS,SubjectDB


# Create your views here.
def index(request):
    return render(request, 'Login/login.html')

#
# def handlelogin(request):
#     if request.method == 'POST':
#         loginusername = request.POST['email']
#         loginpass = request.POST['password']
#         user = authenticate(username=loginusername,password = loginpass)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"Successfully Logged In")
#             return HttpResponse("Redirecting")
#         else:
#             messages.error(request,"Invalid Credentials")
#             return HttpResponse("srry failed login{% csrf_token %}")
#
# def handlelogout(request):
#     if request.method == 'GET':#Change it to POST
#         logout(request)
#         messages.success(request,'Successfully Logged Out')
#         return redirect('Home')
#     else:
#         return redirect('Home')

def handleloginuser(request):
    if request.method == 'POST':
        loginuser  = request.POST['email']
        loginusername = loginuser.lower()
        loginpass = request.POST['password']
        try:
            user = AdminUSERS.objects.get(email=loginusername)
        except AdminUSERS.DoesNotExist:
            messages.success(request, 'User Doesnt Exists ')
            return redirect("HomePage")

         # Store user info in session
        request.session['user_id'] = user.email
        request.session['username'] = user.username

        # Compare the passwords
        if user.password == loginpass :
            if user.usertype.startswith("ad"):
                messages.success(request, 'Welcome Dear  ' + ' ' + user.username)
                return redirect("HomePage")
            else:
                # return redirect('Login/login/')
                messages.success(request,'Welcome Dear  '+' '+user.username)
                return redirect("TeachersHome")
        else:
            messages.error(request,"User Id Exists But Wrong password Entered")
            return redirect('LogInPage')

def handlelogoutuser(request):
    try:
        del request.session['user_id']  # Delete user session
    except KeyError:
        pass
       # Redirect to login page
    messages.success(request,'You have been successfully logged out')
    return redirect("HomePagehome")

