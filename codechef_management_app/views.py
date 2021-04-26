from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from codechef_management_app.models import Events
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

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("/")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect("/")
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
        role_id = "2"

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("/")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect("/")
            else:
                user = User.objects.create_user(role_id = role_id,username=username ,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
                user.save();
                messages.info('Member Successfully Added !')
                return redirect('events')
        else:
            messages.info(request,"Password not Macthing...")
            return redirect('/')
        return redirect('/')
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


# def events(request):
#     return render(request,"events.html")

# def events(request):
#     if request.method == "POST":
#         return render(request,"events.html")
#     else:
#         return HttpResponse("Hello")
#         event = Events.objects.all()
#         return render(request,'codechef_management_app/events.html',{'eve':event})

def events(request):
    event = Events.objects.all()
    return render(request,'events.html',{'eve':event})



def event_form(request): 
    if request.method == "POST":
        event_id = request.POST['event_id']
        title = request.POST['title']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        if event_id == event_id:
            if User.objects.filter(event_id=event_id).exists():
                messages.info(request,'Event ID Taken')
                return redirect("event_form")
            else:
                eventss = Events.objects.create_user(description = description,start_date=start_date ,end_date=end_date,event_id=event_id,title=title)
                eventss.save();
                messages.info('Event Added!')
                return redirect('event_form')
        else:
            # messages.info(request,"Password not Macthing...")
            return redirect('event_form')
        return redirect('event_form')
    else:
        return render(request,"event_form.html")

