from rest_framework.response import Response
from rest_framework.views import APIView

from mongo_db_crud.apis.models import Student


class StudentApis(APIView):
    def post(self, request):
        try:
            roll_no = request.data.get('roll_no')
            name = request.data.get('name')
            degree = request.data.get('degree')
            cgpa = request.data.get('cgpa')
            semesters_details = request.data.get('semesters_details')
            student = Student(roll_no=roll_no, name=name, degree=degree, cgpa=cgpa, semesters_details=semesters_details)
            student.save()
            response = {
                'status_code': 200,
                'success': True,
                'message': 'Student is added successfully'
            }
            return Response(response, 200)
        except Exception as e:
            response = {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }
            return Response(response, 500)

    def get(self, request):
        try:
            roll_no = request.data.get('roll_no')
            student = Student.objects(roll_no=roll_no)
            if student:
                response = {
                    'status_code': 200,
                    'success': True,
                    'data': student.first().to_dict()
                }
                return Response(response, 200)
            else:
                response = {
                    'status_code': 200,
                    'success': True,
                    'message': 'No student is found'
                }
                return Response(response, 200)
        except Exception as e:
            response = {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }
            return Response(response, 500)

    def put(self, request):
        """
        To update student insert updated student data with same roll_no
        :return:
        """
        pass

    def delete(self, request):
        try:
            roll_no = request.data.get('roll_no')
            student = Student.objects(roll_no=roll_no)
            if student:
                student.delete()
                response = {
                    'status_code': 200,
                    'success': True,
                    'message': 'Student is deleted successfully'
                }
                return Response(response, 200)
            else:
                response = {
                    'status_code': 200,
                    'success': True,
                    'message': 'Student does not exist'
                }
                return Response(response, 200)
        except Exception as e:
            response = {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }
            return Response(response, 500)