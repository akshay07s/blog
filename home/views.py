from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    a=random.randint(1,8)
    param={'a':a}
    return render(request,'home/home.html',param)
# Create your views here.

def userlogin(request):
    if request.method=='POST':
        userlogin=request.POST['userlogin']
        passlogin=request.POST['passlogin']

        ouruser = authenticate(request,username=userlogin,password=passlogin)
       

        if ouruser is not None:
           
            login(request,ouruser)
            messages.success(request,'Successfully LogIn')
            return redirect('/blog/')
        else:
            messages.error(request,'INVALID USER')
    return render(request,'home/login.html')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
       
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
            return redirect('/signup')
        if pass1!=pass2:
            messages.error(request,"Passwords not match")
            return redirect('/signup')
        if not username.isalnum():
            messages.info(request,'Username Contain only letters and numbers')
            return redirect('/signup')
        else:
            messages.success(request,'Successfully registered')
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            return redirect('/userlogin')
    return render(request, 'home/signup.html')

def userlogout(request):
    logout(request)
    return redirect('/')

def contact(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        contact = Contact(name=name,email=email,phone=phone,context=message)
        contact.save()
    return render(request,'home/contact_us.html')