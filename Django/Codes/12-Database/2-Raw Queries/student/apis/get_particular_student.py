from rest_framework.views import APIView
from rest_framework.response import Response

from student.repository import StudentRepository


class GetParticularStudent1(APIView):
    def get(self, request):
        # get request arguments
        username = request.data.get('username', '')

        # initialize repos
        student_repo = StudentRepository()

        # get particular student from database
        student = student_repo.get_particular_student(username)
        if student:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'student': student
                }
            }
        else:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'student is not found'
                }
            }
        return Response(final_response)
