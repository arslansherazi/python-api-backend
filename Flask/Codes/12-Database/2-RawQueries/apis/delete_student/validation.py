from flask_restful import reqparse

delete_student_parser = reqparse.RequestParser()

delete_student_parser.add_argument('username', required=True)
