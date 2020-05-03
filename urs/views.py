from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    st = "<a href='/register'>Register</a> <a href='/login'>Login</a>"
    return HttpResponse(st)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        user= User.objects.create_user(username=username,email=email,password=password,first_name=first_name, last_name=last_name)
        user.save();
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"project.html")
        else: 
            print("incoreect")
            messages.add_message(request, messages.INFO, 'Hello world.')

            messages.error(request,"Invalid Credentials")
            return redirect('/')
    
    else:
        return render(request,'login.html')

#def project(request):
    
