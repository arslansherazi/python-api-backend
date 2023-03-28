from django.shortcuts import render

def index(request):
    name = 'Arslan Haider Sherazi'
    cgpa = 3.42
    array = [1, 2, 3, 4, 5]
    return render(request, "index.html", {'name':name, 'cgpa':cgpa, 'array':array})
