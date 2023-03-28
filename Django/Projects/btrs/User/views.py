from django.shortcuts import render,redirect
from User.models import Reservations
from Guest.models import Friend,Feedbacks,User,Fares,Schedule
from django.views.decorators.cache import never_cache,cache_control

                                    #### Web pages views #####
def loader(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        return render(request, "User/user_loader.html", {})


def home(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        username=request.session['user']
        return render(request, "User/Home.html", {"username":username})

def faqs(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        username=request.session['user']
        return render(request, "User/FAQs.html", {"username":username})


def friend(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        username=request.session['user']
        data = User.objects.values("Name","Email").get(Username=request.session['user'])
        return render(request, "User/Friend.html", {"username":username,"data":data})


def feedback(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        username=request.session['user']
        data = User.objects.values("Name", "Email", "Contact", "Age", "Gender").get(Username=request.session['user'])
        return render(request, "User/Feedback.html", {"username":username,"data":data})


@never_cache
def logout(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        del request.session['user']
        return redirect("/Guest/loader")


@never_cache
def myReservations(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        try:
            res=Reservations.objects.filter(Username=request.session['user'])
            #we can use the following syntax for same purpose
            #res=Reservations.objects.all().get(Username=request.session['user'])
        except Reservations.DoesNotExist:
            res = None
        return render(request, "User/Reservations.html", {"username":request.session['user'],"res": res})


def fareList(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        fares = Fares.objects.all()
        return render(request, "User/Fares.html", {"username":request.session['user'],"fares": fares})

def logout(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        del request.session['user']
        return redirect("/Guest/logout")

def changePassword(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        return render(request, "User/change_password.html", {"username":request.session['user']})


def ticketBookingURL(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        b = Schedule.objects.all()
        return render(request, "User/user_ticket.html", {"buses": b})



def profileUpdate(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        profile=User.objects.get(Username=request.session['user'])
        return render(request, "User/profile_update.html", {"profile": profile})






                                    #### Forms Handling vies ####

def friendForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        fn = request.POST.get('fname')
        fe = request.POST.get('femail')
        c = request.POST.get('comments')

        friend=Friend(Name=n, Email=e, FName=fn, FEmail=fe, Comments=c)
        friend.save()

        username = request.session['user']
        return render(request, "User/successful_friend.html", {"username":username})



def feedbackForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        f = request.POST.get('feedback')

        f=Feedbacks(Name=n, Email=e, Contact=c, Age=a, Gender=g, Feedback=f)
        f.save()

        username = request.session['user']
        return render(request, "User/successful_feedback.html", {"username":username})


def changePasswordForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        o = request.POST.get('old')
        n = request.POST.get('neww')

        user = User.objects.get(Password=o)
        if not user:
            return render(request, "User/user_unsuccessful_password_change.html", {"username":request.session['user']})
        else:
            user.Password=n
            user.save()
            return render(request, "User/user_successful_password_change.html", {"username":request.session['user']})


def ticketBooking(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('fro')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')

        try:
            ticket=Reservations.objects.all().get(Username=request.session['user'],From=f,To=t)
        except:
            Reservations.DoesNotExist
            ticket=None

        if not ticket:
            return render(request, "User/user_ticket_booking.html", {"username": request.session['user'],"From":f, "To":t, "Date":d, "Dept":de, "Arri":a})
        else:
            return render(request, "User/user_ticket_final.html", {"username": request.session['user'],"data":ticket})


def ticketBookingForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        token = request.POST.get('token')
        f = request.POST.get('fro')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')
        s=request.POST.get('seats')

        if(token=='1'):#used for ticket booking form

            try:
                ticket = Reservations.objects.all().get(Username=request.session['user'], From=f, To=t)
                # we can use the following syntax for same purpose
                # res=Reservations.objects.filter(Username=request.session['user'])
            except:
                Reservations.DoesNotExist
                ticket = None

            if not ticket:
                try:
                    res = Reservations(Username=request.session['user'], From=f, To=t, Date=d, Departure=de, Arrival=a,Seats=s)
                except:
                    Reservations.DoesNotExist
                    res = None
                username = request.session['user']
                if(res.save()):
                    return render(request, "User/user_unsuccessful_ticket.html", {"username": username})
                else:
                    return render(request, "User/user_successful_ticket.html", {"username": username})

            else:
                return render(request, "User/user_ticket_final.html", {"username": request.session['user'], "data": ticket})

        else:#used for reservation editing form
            try:
                res = Reservations.objects.get(Username=request.session['user'], From=f, To=t)
                res.Seats = s
                res.save()
            except:
                Reservations.DoesNotExist
                res = None
            return render(request, "User/user_reservation_edit_successful.html", {"username": request.session['user']})




def reservationsOptions(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        f = request.POST.get('from')
        t = request.POST.get('to')
        d = request.POST.get('date')
        de = request.POST.get('dept')
        a = request.POST.get('arri')
        s = request.POST.get('seats')

        if 'edit' in request.POST:
            return render(request, "User/user_reservation_edit.html", {"username": request.session['user'],"From":f, "To":t, "Date":d, "Dept":de, "Arri":a, "Seats":s} )
        else:
            res = Reservations.objects.get(Username=request.session['user'],From=f,To=t)
            res.delete()
            return render(request, "User/user_reservation_delete_successful.html", {})


@never_cache
def profileUpdateForm(request):
    if request.session.has_key('admin'):
        return redirect("/Admin/home")
    elif not request.session.has_key('user'):
        return redirect("/Guest/index")
    else:
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        pro = request.POST.get('province')
        city = request.POST.get('city')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        add = request.POST.get('address')

        user = User.objects.get(Username=request.session['user'])
        user.Name=n
        user.Email=e
        user.Contact=c
        user.Province=pro
        user.City=city
        user.Age=a
        user.Gender=g
        user.Address=add
        user.save()

        return render(request, "User/user_successful_update_profile.html", {"username":request.session['user']})


