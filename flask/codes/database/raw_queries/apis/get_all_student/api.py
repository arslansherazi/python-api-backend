from flask_restful import Resource, reqparse

from repository import StudentRepository


class GetAllStudents(Resource):
    def post(self):
        # get data from repository
        student_repo = StudentRepository()
        students = student_repo.get_all_students()
        if students:
            return {
                'students': students
            }
        return {
            'message': 'No student is added yet'
        }
