from flask_restful import Resource, reqparse

from apis.get_particular_student.validation import get_student_parser
from repository import StudentRepository


class GetParticularStudents(Resource):
    parser = get_student_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        username = args['username']

        # get data from repository
        student_repo = StudentRepository()
        student = student_repo.get_particular_student(username)
        if student:
            return {
                'student': student
            }
        return {
            'message': 'No student is found'
        }
