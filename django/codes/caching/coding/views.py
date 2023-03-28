from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache #used to avoid saving of requested page in cache.
def index(request):
    if request.session.has_key('username'):
        return redirect("/coding/loggedinPage")
    else:
        return render(request, "index.html", {})

@never_cache #Every time page is requested by user, It will be loaded directly from server instead of cache
def loggedinPage(request):
    if request.session.has_key('username'):
        user = request.session['username']
        return render(request, "loggedin_page.html", {'user' : user})
    else:
        return redirect("/coding/index")

def loginForm(request):
    user = request.POST['username']
    request.session['username'] = user

    return redirect("/coding/loggedinPage")


def logout(request):
    if request.session.has_key('username'):
        del request.session['username']

    return redirect("/coding/index")
