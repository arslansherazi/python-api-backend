from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html", {})

def form1(request):
    return render(request, "form1.html", {})

def form2(request):
    return render(request, "form2.html", {})

def success1(request):
    username  = request.session.get('username')
    password  = request.session.get('password')
    return render(request, "success1.html", {'username' : username, 'password' : password})

def success2(request):
    name   = request.session.get('name')
    rollno = request.session.get('rollno')
    degree = request.session.get('degree')
    cgpa   = request.session.get('cgpa')
    return render(request, "success2.html", {'name' : name, 'rollno' : rollno, 'degree' : degree, 'cgpa' : cgpa})

#### Forms Handling ####
#method=post
def form1Handling(request):#make sure that values of name attributes of form input fields should be same as arguments of get functions
    u = request.POST['username'] #request.POST.get('username') => We can also use this syntax but only in case of post method
    p = request.POST['password']

    request.session['username'] = u
    request.session['password'] = p

    print(request.session['username'])

    return redirect("/coding/success1")

#method=get
def form2Handling(request):#make sure that values of name attributes of form input fields should be same as arguments of get functions
    n  = request.GET['name']
    rn = request.GET['rollno']
    d  = request.GET['degree']
    c  = request.GET['cgpa']

    request.session['name']   = n
    request.session['rollno'] = rn
    request.session['degree'] = d
    request.session['cgpa']   = c

    return redirect("/coding/success2")
