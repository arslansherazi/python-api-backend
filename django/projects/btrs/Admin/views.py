from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from Guest.models import User,Friend,Feedbacks,Schedule,Fares,Admin
from User.models import Reservations
from django.views.decorators.cache import never_cache,cache_control




                                #Web Pages Views
@never_cache
def loader(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/loader.html", {})


@never_cache
def home(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/Home.html", {})


@never_cache
def logout(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        del request.session['admin']
        return redirect("/Guest/loader")


@never_cache
def register(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/Register.html", {})


@never_cache
def faqs(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/faqs.html", {})


@never_cache
def tellAFriend(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        friends = Friend.objects.all()
        return render(request, "Admin/friend.html", {"friends": friends})


@never_cache
def feedback(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = Feedbacks.objects.all()
        return render(request, "Admin/feedback.html", {"feedback": f})


@never_cache
def users(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        u = User.objects.all()
        return render(request, "Admin/users.html", {"users": u})


@never_cache
def buses(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        b = Schedule.objects.all()
        return render(request, "Admin/buses.html", {"buses": b})


@never_cache
def newBus(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/buses_new.html", {})


@never_cache
def fares(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = Fares.objects.all()
        return render(request, "Admin/fares.html", {"fares": f})


@never_cache
def newFare(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/fares_new.html", {})


@never_cache
def changePassword(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        return render(request, "Admin/change_password.html", {})


def reservations(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        r = Reservations.objects.all()
        return render(request, "Admin/reservations.html", {"res": r})






                                        #Forms Handling Views
@never_cache
def registerUser(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
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

        return render(request, "Admin/admin_successful_registeration.html", {})


@never_cache
def friendOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        fn = request.POST.get('fname')
        fe = request.POST.get('femail')
        c = request.POST.get('comments')

        #Handling multiple submit buttons."view"=submit button name
        if 'view' in request.POST:
            data={'Name':n, 'Email':e, 'FName':fn, 'FEmail':fe, 'Comments':c}
            return render(request, "Admin/friend_options.html", {'data':data})
        else:
            f=Friend.objects.get(Name=n,Email=e,FName=fn,FEmail=fe,Comments=c)
            f.delete()
            return render(request, "Admin/friend_cancel.html", {})


@never_cache
def friendApproval(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        fn = request.POST.get('fname')
        fe = request.POST.get('femail')
        c = request.POST.get('comments')
        mail=c+'\nMail from'+n
        res=send_mail("Hello"+fn,mail,settings.EAIL_HOST_USER,[settings.EMAIL_HOST_USER,'arslanhaider95@hotmail.com'])
        return render(request, "Admin/friend_approval.html", {'res':res})


@never_cache
def feedbackOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        f = request.POST.get('feedback')

        if 'view' in request.POST:
            data = {'Name': n, 'Email': e, 'Contact': c, 'Age': a, 'Gender': g, 'Feedback':f}
            return render(request, "Admin/feedback_options.html", {'data': data})
        else:
            fe  = Feedbacks.objects.get(Name=n, Email=e, Contact=c, Age=a, Gender=g, Feedback=f)
            fe.delete()
            return render(request, "Admin/feedback_cancel.html", {})


@never_cache
def usersOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        id = request.POST.get('id')
        user=User.objects.get(Username=id)

        if 'view' in request.POST:
            return render(request, "Admin/users_options.html", {'data': user})
        else:
            user = User.objects.get(Username=id)
            user.delete()
            return render(request, "Admin/users_delete.html", {})


@never_cache
def busesOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('from')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')
        bus={'From':f, 'To':t, 'Date':d, 'Dept':de, 'Arri':a}
        print(a)
        if 'edit' in request.POST:
            return render(request, "Admin/buses_edit.html", {'data':bus})
        else:
            bus = Schedule.objects.get(From=f, To=t, Date=d, Departure=de, Arrival=a)
            bus.delete()
            return render(request, "Admin/buses_delete.html", {})


@never_cache
def editBus(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('from')
        t = request.POST.get('to')
        d = request.POST.get('date')
        d1 = request.POST.get('date1')
        de = request.POST.get('dept')
        de1 = request.POST.get('dept1')
        a = request.POST.get('arri')
        a1 = request.POST.get('arri1')

        b=Schedule.objects.get(From=t, To=t, Date=d1, Departure=de1, Arrival=a1)
        b.Date=d
        b.Departure=de
        b.Arrival=a
        b.save()
        return render(request, "Admin/admin_successful_edit_bus.html", {})


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def newBusForm(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('fro')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')

        b=Schedule(From=f, To=t, Date=d, Departure=de, Arrival=a)
        b.save()

        return render(request, "Admin/admin_successful_schedule_bus.html", {})


@never_cache
def faresOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('from')
        t = request.POST.get('to')
        fa = request.POST.get('fare')

        fare={'From':f, 'To':t, 'Fare':fa,}
        if 'edit' in request.POST:
            return render(request, "Admin/fares_edit.html", {'data':fare})
        else:
            far = Fares.objects.get(From=f, To=t, Fare=fa)
            fare.delete()
            return render(request, "Admin/fares_delete.html", {})


@never_cache
def editFare(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('from')
        t = request.POST.get('to')
        fa = request.POST.get('fare')
        fa1 = request.POST.get('fare1')

        f=Fares.objects.get(From=t, To=t, Fare=fa1)
        f.Fare=fa
        f.save()
        return render(request, "Admin/admin_successful_edit_fare.html", {})


@never_cache
def newFareForm(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('fro')
        t = request.POST.get('to')
        fa = request.POST.get('fare')

        fare=Fares(From=f, To=t, Fare=fa)
        fare.save()

        return render(request, "Admin/admin_successful_schedule_fare.html", {})


@never_cache
def changePasswordForm(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        o = request.POST.get('old')
        n = request.POST.get('neww')

        admin = Admin.objects.get(Password=o)
        if not admin:
            return render(request, "Admin/admin_unsuccessful_password_change.html", {})
        else:
            admin.Password=n
            admin.save()
            return render(request, "Admin/admin_successful_password_change.html", {})


def reservationsOptions(request):
    if request.session.has_key('user'):
        return redirect("/User/home")
    elif not request.session.has_key('admin'):
        return redirect("/Guest/index")
    else:
        u = request.POST.get('uId')
        f = request.POST.get('from')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')
        s = request.POST.get('seats')

        r = Reservations.objects.get(Username=u, From=f, To=t, Date=d, Departure=de, Arrival=a,Seats=s)
        r.delete()

        return render(request, "Admin/admin_successful_cancel_reservation.html", {})
