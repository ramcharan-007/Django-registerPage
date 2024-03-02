from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    return HttpResponse("Home")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        # userImage = request.POST['userimage']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firsttname = fname
        myuser.lastname = lname

        myuser.save()

        messages.success(request,"Your account is created sucesfully")

        return redirect('login')
    
    return render(request, 'signup.html')
    
def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request, user)
            return render(request, "dashbord.html", {"user" : user})
        else:
            messages.error(request, "Bad credentials!")
            return render(request, "login.html")
        
    return render(request, 'login.html')

def dashboard(request):
    pass