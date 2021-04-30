from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from codechef_management_app.models import Events
from django.db import connection
User = get_user_model()


# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")


def register(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        codechef_id = request.POST['codechef_id']
        email = request.POST['email']
        prn = request.POST['prn']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # is_staff = "0"


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username ,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
                user.save();
                print('User created')
                return redirect('login')
        else:
            messages.info(request,"Password not Macthing...")
            return redirect('/')
        return redirect('/')
    else:
        return render(request,"register.html")



def executive_register(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        codechef_id = request.POST['codechef_id']
        email = request.POST['email']
        prn = request.POST['prn']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # role_id = "2"
        is_staff = "1"

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("executive_register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect("executive_register")
            else:
                user = User.objects.create_user(is_staff=is_staff,username=username ,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
                user.save();
                # messages.info('Member Successfully Added !')
                return redirect('events')
        else:
            messages.info(request,"Password not Macthing...")
            return redirect('executive_register')
    else:
        return render(request,"executive_register.html")



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("events")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,"login.html")


def logoutt(request):
    auth.logout(request)
    return redirect("/")

def events(request):
    event = Events.objects.order_by('-start_date')
    return render(request,'events.html',{'eve':event})


def event_form(request): 
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        eventss = Events.objects.create(description = description,start_date=start_date ,end_date=end_date,title=title)
        eventss.save();
        return redirect('events')

    else:
        return render(request,"event_form.html")


def event_del(request): 
    if request.method == "POST":
        title = request.POST['title']
        Events.objects.filter(title=title).delete()
        # eventss = Events.objects.delete(event_id=event_id)
        return redirect('events')
    else:
        return render(request,"event_del.html")


def executive_del(request):
    if request.method == "POST":
        username = request.POST['username']
        User.objects.filter(username=username).delete()
        return redirect('events')
    else:
        return render(request,"executive_del.html")


def participants_del(request):
    if request.method == "POST":
        username = request.POST['username']
        User.objects.filter(username=username).delete()
        return redirect('events')
    else:
        return render(request,"participants_del.html")