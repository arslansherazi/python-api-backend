from flask_restful import Resource, reqparse

from repository import StudentRepository
from apis.add_student.validation import add_student_parser


class AddStudent(Resource):
    parser = add_student_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        username = args['username']
        name = args['name']
        degree = args['degree']
        cgpa = args['cgpa']

        # get data from repository
        student_repo = StudentRepository()
        student_added = student_repo.add_student(username, name, degree, cgpa)
        if student_added:
            return {
                'message': 'student is added successfully'
            }
        return {
            'message': 'Something went wrong. Try Later'
        }

