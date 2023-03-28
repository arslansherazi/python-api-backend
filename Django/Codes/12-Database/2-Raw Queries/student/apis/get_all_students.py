from rest_framework.views import APIView
from rest_framework.response import Response

from student.models import Student
from student.repository import StudentRepository


class GetAllStudents(APIView):
    def get(self, request):
        # initialize repos
        student_repo = StudentRepository()

        # delete student from database
        students = student_repo.get_all_students()
        if students:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'students': students
                }
            }
        else:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'No student is added yet'
                }
            }
        return Response(final_response)
