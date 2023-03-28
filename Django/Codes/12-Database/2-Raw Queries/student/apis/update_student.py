from rest_framework.views import APIView
from rest_framework.response import Response

from student.repository import StudentRepository


class UpdateStudent(APIView):
    def put(self, request):
        # get request arguments
        username = request.data.get('username', '')
        name = request.data.get('name', '')
        degree = request.data.get('degree', '')
        cgpa = request.data.get('cgpa', '')

        # initialize repos
        student_repo = StudentRepository()

        # delete student from database
        is_student_updated = student_repo.update_student(username, name, degree, float(cgpa))
        if is_student_updated:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'student is updated successfully'
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
