from django.shortcuts import render, HttpResponse
import json

from Coding.models import Student, StudentSchema


def index(request):
    return render(request, "index.html", {})


def noJS(request):
    return render(request, "noJS.html", {})


def addStudent(request):
    roll_no = request.POST["roll_no"]
    name = request.POST["name"]
    degree = request.POST["degree"]
    cgpa = request.POST["cgpa"]

    student = Student(roll_no=roll_no, name=name, degree=degree, cgpa=cgpa)
    student.save()
    return HttpResponse("Student is added successfully")


def getAllStudents(request):
    students = Student.objects.all()
    if students:
        schema = StudentSchema(many=True)#many=True is used to serialize multiple objects
        students_serialized = schema.dump(students)
        students_json = students_serialized[0]
        return HttpResponse(json.dumps(students_json))
    else:
        return HttpResponse("no students in the database yet")


def searchStudent(request):
    roll_no = request.GET["roll_no"]

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Student.DoesNotExist:
        student = None

    if student:
        schema = StudentSchema()
        student_serialized = schema.dump(student)
        student_json = student_serialized[0]
        return HttpResponse(json.dumps(student_json))#json.dumps() converts JSON into string JSON(which is required at front end jQuery)
    else:
        return HttpResponse("no student found")


def deleteStudent(request):
    roll_no = request.GET["roll_no"]
    student = Student.objects.get(roll_no=roll_no)
    student.delete()
    return HttpResponse("Student is deleted successfully")


def updateStudent(request):
    roll_no = request.POST["roll_no"]
    name = request.POST["name"]
    degree = request.POST["degree"]
    cgpa = request.POST["cgpa"]

    student = Student.objects.get(roll_no=roll_no)
    student.name = name
    student.degree = degree
    student.cgpa = cgpa
    student.save()

    return HttpResponse("success")
