from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apis.serializers import StudentSerializer, UsernameSerializer
from apis.models import Student


# Function based api
@api_view(["GET"])
def get_student(request):
    serializer = UsernameSerializer(data=request.data)
    if serializer.is_valid():
        student = Student.objects.get(username=request.data["username"])
        if student:
            serialized_student = StudentSerializer(student)
            return Response({"data": serialized_student.data})
        else:
            return Response({"message": "Student does not exist"})
    else:
        return Response({"message": serializer.errors})


# class based apis
class StudentApis(APIView):
    # Add new student into database
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()  # Deserialization
            try:
                student.save()  # insert student into database
                return Response({"message": "student is added successfully"})
            except:
                return Response({"message": "Sorry, There is a problem. Try later"})
        else:
            return Response({"message": serializer.errors})

    # get all students from database
    def get(self, request):
        students = Student.objects.all()
        if students:
         serialized_objects = StudentSerializer(students, many=True)
         return Response(serialized_objects.data)
        else:
            return Response({"message": "no student is added yet"})

    # update student
    def put(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = Student.objects.get(username=request.data["username"])
            if student:
                serializer.instance = student
                serializer.initial_data = request.data
                if serializer.is_valid():
                    updated_student = serializer.save()
                    try:
                        updated_student.save()  # update student in database
                        return Response({"message": "student is updated successfully"})
                    except:
                        return Response({"message": "Sorry, There is a problem. Try later"})
                else:
                    return Response({"message": serializer.errors})
            else:
                return Response({"message": "Student does not exist"})
        else:
            return Response({"message": serializer.errors})

    # delete student
    def delete(self, request):
        serializer = UsernameSerializer(data=request.data)
        if serializer.is_valid():
            student = Student.objects.get(username=request.data["username"])
            if student:
                try:
                    student.delete()  # delete student from database
                    return Response({"message": "student is deleted successfully"})
                except:
                    return Response({"message": "Sorry, There is a problem. Try later"})
            else:
                return Response({"message": "Student does not exist"})
        else:
            return Response({"message": serializer.errors})
