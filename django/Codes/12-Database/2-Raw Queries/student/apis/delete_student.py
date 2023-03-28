from rest_framework.views import APIView
from rest_framework.response import Response

from student.repository import StudentRepository


class DeleteStudent(APIView):
    def delete(self, request):
        # get request arguments
        username = request.data.get('username', '')

        # initialize repos
        student_repo = StudentRepository()

        # delete student from database
        is_student_deleted = student_repo.delete_student(username)
        if is_student_deleted:
            final_response = {
                'message': 'success',
                'success': True,
                'status_code': 200,
                'data': {
                    'message': 'student is deleted successfully'
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
