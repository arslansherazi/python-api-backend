from flask_restful import reqparse

update_student_parser = reqparse.RequestParser()

update_student_parser.add_argument('username', required=True)
update_student_parser.add_argument('name', required=True)
update_student_parser.add_argument('degree', required=True)
update_student_parser.add_argument('cgpa', required=True, type=float)
