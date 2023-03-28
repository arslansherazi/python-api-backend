from rest_framework.views import APIView
from rest_framework.response import Response

from student.repository import StudentRepository


class AddStudent(APIView):
    def post(self, request):
        # get request arguments
        username = request.data.get('username', '')
        name = request.data.get('name', '')
        degree = request.data.get('degree', '')
        cgpa = request.data.get('cgpa', '')

        # initialize repos
        student_repo = StudentRepository()

        # add student into database
        is_student_added = student_repo.add_student(username, name, degree, float(cgpa))
        if is_student_added:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'student is added successfully'
                }
            }
        else:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'Sorry, there is a problem with system. Try again later'
                }
            }
        return Response(final_response)
