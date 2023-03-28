from rest_framework.views import APIView
from rest_framework.response import Response

from student.repository import StudentRepository


class GetParticularStudent2(APIView):
    def get(self, request):
        # get request arguments
        degree = request.data.get('degree', '')
        cgpa = request.data.get('cgpa', '')

        # initialize repos
        student_repo = StudentRepository()

        # get particular students from database
        students = student_repo.get_particular_student_by_degree_and_cgpa(degree, float(cgpa))
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
                    'message': 'no student is found'
                }
            }
        return Response(final_response)
