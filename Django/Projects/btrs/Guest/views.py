from django.shortcuts import render,redirect
from django.http import HttpResponse
from Guest.models import User,Friend,Feedbacks,Schedule,Fares,Admin
from django.http import JsonResponse
from django.views.decorators.cache import never_cache,cache_control
import time


                                # Practice
def firstPage(request):
	text="<h1>My First Django Web page<h1>"
	return HttpResponse(text)


def urlParameters(request,p1,p2):
	text="<h1>p1=%s p2=%s<h1>"%(p1,p2)
	return HttpResponse(text)


def hello(request):
	today=time.strftime("%d/%m/%Y")
	daysOfWeek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	return render(request, "hello.html", {"today":today , "dow":daysOfWeek})




                                            #Web Pages Views
def index(request):
        if request.session.has_key('admin'):
            return redirect("/Admin/home")
        elif request.session.has_key('user'):
            return redirect("/User/home")
        else:
            return render(request, "index.html", {})


def register(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "Register.html", {})


def faqs(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "FAQs.html", {})


def friend(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "Friend.html", {})


def feedback(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "Feedback.html", {})


def guestLogin(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "Login.html", {})

@never_cache
def loader(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        return render(request, "guest_loader.html", {})


def busSchedule(request):#view name and model name should be different when working together.For Example we cannot use "Schedule" for both our model and view in this case.
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        buses = Schedule.objects.all()
        return render(request, "Schedule.html", {"buses":buses})


def fares(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        fares = Fares.objects.all()
        return render(request, "Fares.html", {"fares":fares})


def checkUsername(request,u):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        values = User.objects.values('Username')
        for v in values:
            if (u == v['Username']):
                return HttpResponse("yes")

        return HttpResponse("no")




                                                    #Forms Handling Views
def login(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        u = request.POST.get('user')
        p = request.POST.get('password')

        if(u=="admin"):
            admin = Admin.objects.values('Password')
            for a in admin:
                if(p==a["Password"]):
                    request.session['admin'] = u
                    return redirect("/Admin/loader")
            return render(request, "login_error.html", {})
        else:
            values=User.objects.values('Username','Password')
            for v in values:
                if(u==v['Username'] and p==v['Password']):
                    request.session['user']=u
                    return redirect("/User/loader")

        return render(request, "login_error.html", {})



def registerUser(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        u    =  request.POST.get('user')
        p    =  request.POST.get('pass')
        n    =  request.POST.get('name')
        e    =  request.POST.get('email')
        c    =  request.POST.get('contact')
        pro  =  request.POST.get('province')
        city =  request.POST.get('city')
        a    =  request.POST.get('age')
        g    =  request.POST.get('gender')
        add  =  request.POST.get('address')

        user = User(Username=u, Password=p, Name=n, Email=e, Contact=c, Province=pro, City=city, Age=a, Gender=g, Address=add)
        user.save()

        return render(request, "successful_registeration.html", {})


def tellAFriend(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        fn = request.POST.get('fname')
        fe = request.POST.get('femail')
        c = request.POST.get('comments')

        friend=Friend(Name=n, Email=e, FName=fn, FEmail=fe, Comments=c)
        friend.save()

        return render(request, "successful_friend.html", {})


def feedbackForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif request.session.has_key('user'):
        return redirect("/User/home")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        f = request.POST.get('feedback')

        f=Feedbacks(Name=n, Email=e, Contact=c, Age=a, Gender=g, Feedback=f)
        f.save()
        return render(request, "successful_feedback.html", {})

