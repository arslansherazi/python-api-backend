from flask_restful import reqparse

get_student_parser = reqparse.RequestParser()

get_student_parser.add_argument('username', required=True)
