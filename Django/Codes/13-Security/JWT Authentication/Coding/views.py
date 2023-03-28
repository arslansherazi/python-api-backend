from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
import requests
from django.contrib.auth.models import User


from Coding.serializers import StudentSerializer
from Coding.models import Student


@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def get_student(request):  # get details of particular student
    username = request.user.username  # get username from jwt token
    try:
        student = Student.objects.get(username=username)
    except Exception as e:
            return Response({"message": str(e)})
    else:
        if student:
            serialized_student = StudentSerializer(student)
            return Response({"data": serialized_student.data})
        else:
            return Response({"message": "Student does not exist"})


@api_view(["POST"])
def register_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        student = serializer.save()  # Deserialization
        try:
            # create authentication user (it will be saved in auth_user table)
            User.objects.create_user(username=student.username, password=student.password)
            params = {"username": student.username, "password": student.password}  # auth user
            response = requests.post('http://127.0.0.1:8000/Student/api/token', data=params)
            tokens = response.text.split(',')
            # jwt_refresh_token = tokens[0].split(':')[1]
            # jwt_refresh_token = jwt_refresh_token[1:len(jwt_refresh_token) - 1]
            jwt_access_token = tokens[1].split(':')[1]
            jwt_access_token = jwt_access_token[1:len(jwt_access_token)-2]
            student.save()  # insert student into database
            '''return Response({
                "message": "student is added successfully",
                "jwt_access_token": jwt_access_token,
                "jwt_refresh_token": jwt_refresh_token
            })'''
            return Response({
                "message": "student is added successfully",
                "jwt_access_token": jwt_access_token,
            })
        except Exception as e:
            return Response({"message": str(e)})
    else:
        return Response({"message": "Student already exist"})


class StudentApis(APIView):
    permission_classes = (IsAuthenticated,)

    # get all students from database
    def get(self, request):
        try:
            students = Student.objects.all()
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if students:
                serialized_objects = StudentSerializer(students, many=True)
                return Response(serialized_objects.data)
            else:
                return Response({"message": "no student is added yet"})

    # update student
    def put(self, request):
        username = request.user.username  # get username from jwt token
        try:
            student = Student.objects.get(username=username)
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if student:
                serializer = StudentSerializer(student, data=request.data)
                if serializer.is_valid():
                    updated_student = serializer.save()
                    try:
                        updated_student.save()  # update student in database
                        return Response({"message": "student is updated successfully"})
                    except Exception as e:
                        return Response({"message": str(e)})
                else:
                    return Response({"message": "Student does not exist"})

    # delete student
    def delete(self, request):
        username = request.user.username  # get username from jwt token
        try:
            student = Student.objects.get(username=username)
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if student:
                try:
                    student.delete()  # delete student from database
                    return Response({"message": "student is deleted successfully"})
                except Exception as e:
                    return Response({"message": str(e)})
            else:
                return Response({"message": "Student does not exist"})





