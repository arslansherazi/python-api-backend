from django.shortcuts import render, redirect

def index(request):
    if request.session.has_key('username'):
        return redirect("/Coding/loggedinPage")
    else:
        return render(request, "index.html", {})

def loginForm(request):
    if request.session.has_key('username'):
        return redirect("/Coding/index")
    else:
        username = request.POST['username']
        request.session['username'] = username
        return redirect("/Coding/loggedinPage")

def loggedinPage(request):
    if request.session.has_key('username'):
        username = request.session.get('username')
        return render(request, "loggedinPage.html", {'username' : username})
    else:
        return redirect("/Coding/index") 

def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
        return redirect("/Coding/index")
    else:
        return redirect("/Coding/index")
    

