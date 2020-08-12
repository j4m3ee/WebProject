from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def hello(request):
    tags = ['น้ำตก','ทะเล','ภูเขา','หมอก']
    rating=5
    #Query Data From Model
    data = Post.objects.all()
    return render(request,'index.html',
    {
        'name': 'บทความท่องเที่ยว',
        'tags':tags,
        'rating':rating,
        'posts':data
    })

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def loginForm(request):
    return render(request,'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    #check username
    user = auth.authenticate(username=username,password=password)
    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'Username is not found.')
        return redirect('/loginForm')

def logout(requset):
    auth.logout(requset)
    return redirect('/')
    


def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    rePassword = request.POST['rePassword']

    if password == rePassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is already use.')
            print('Username is already use.')
            return redirect('/createform')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email is already use.')
            print('Email is already use.')
            return redirect('/createform')
        else:
            user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request,'Re-Password is wrong.')
        print('Re-Password is wrong.')
        return redirect('/createform')
    

    
