from flask_restful import reqparse


add_student_parser = reqparse.RequestParser()

add_student_parser.add_argument('username', required=True)
add_student_parser.add_argument('name', required=True)
add_student_parser.add_argument('degree', required=True)
add_student_parser.add_argument('cgpa', required=True, type=float)
