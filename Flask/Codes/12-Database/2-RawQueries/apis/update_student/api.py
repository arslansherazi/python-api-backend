from flask_restful import Resource, reqparse

from apis.update_student.validation import update_student_parser
from repository import StudentRepository


class UpdateStudent(Resource):
    parser = update_student_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        username = args['username']
        name = args['name']
        degree = args['degree']
        cgpa = args['cgpa']

        # get data from repository
        student_repo = StudentRepository()
        student_updated = student_repo.update_student(username, name, degree, cgpa)
        if student_updated:
            return {
                'message': 'student is updated successfully'
            }
        return {
            'message': 'Something went wrong. Try Later'
        }
