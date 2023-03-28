from flask_restful import Resource, reqparse

from apis.delete_student.validation import delete_student_parser
from repository import StudentRepository


class DeleteStudent(Resource):
    parser = delete_student_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        username = args['username']

        # get data from repository
        student_repo = StudentRepository()
        student_deleted = student_repo.delete_student(username)
        if student_deleted:
            return {
                'message': 'student is deleted successfully'
            }
        return {
            'message': 'Something went wrong. Try Later'
        }
