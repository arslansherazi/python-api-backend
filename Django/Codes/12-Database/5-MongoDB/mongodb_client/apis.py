from rest_framework.decorators import api_view

from django.conf import settings
from rest_framework.response import Response


@api_view(['POST'])
def add_student(request):
    roll_no = request.data['roll_no']
    name = request.data['name']
    degree = request.data['degree']
    cgpa = request.data['cgpa']

    students_data = settings.STUDENTS_DATA
    student = students_data.find_one({'roll_no': roll_no})
    if not student:
        try:
            students_data.insert_one({
                'roll_no': roll_no,
                'name': name,
                'degree': degree,
                'cgpa': float(cgpa)
            })
            return Response({
                'message': 'Student is added successfully'
            })
        except Exception:
            return Response({
                'message': 'Something is went wrong'
            })
    else:
        return Response({
            'message': 'Student is already present'
        })


@api_view(['GET'])
def get_all_students(request):
    students_data = settings.STUDENTS_DATA
    mongo_students = students_data.find()
    students = []
    for mongo_student in mongo_students:
        student = {
            'roll_no': mongo_student.get('roll_no'),
            'name': mongo_student.get('name'),
            'degree': mongo_student.get('degree'),
            'cgpa': mongo_student.get('cgpa')
        }
        students.append(student)
    return Response({
        'students': students
    })


@api_view(['PUT'])
def update_student(request):
    roll_no = request.data['roll_no']
    cgpa = request.data['cgpa']
    students_data = settings.STUDENTS_DATA
    update_query = {'roll_no': roll_no}
    update_values = {'$set': {'cgpa': float(cgpa)}}
    try:
        students_data.update_one(update_query, update_values)
        return Response({'message': 'Student is updated successfully'})
    except Exception:
        return Response({'message': 'Something went wrong'})


@api_view(['DELETE'])
def delete_student(request):
    roll_no = request.data['roll_no']
    students_data = settings.STUDENTS_DATA
    try:
        students_data.delete_one({'roll_no': roll_no})
        return Response({'message': 'Student is deleted successfully'})
    except Exception:
        return Response({'message': 'Something went wrong'})
