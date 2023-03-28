from flask import jsonify
from flask_restful import Resource, reqparse

from models import *
from app import app


# function based api
from schemas import StudentSchema


@app.route('/api/get_student', methods=['GET'])
def get_student():
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, location='args')  # gets argument from request query string
    args = parser.parse_args()
    try:
        student = Student.query.get(args['username'])
    except Exception as e:
        return {'Exception': str(e)}
    if student:
        student_schema = StudentSchema()
        student_response = student_schema.dump(student).data
        student_response_json = jsonify(student_response)
        return student_response_json
    else:
        return 'Student does not exist'


# class based apis
class StudentApis(Resource):
    # Add new student into database
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)  # gets argument from POST body
        args1 = parser.parse_args()
        try:
            student = Student.query.get(args1['username'])
        except Exception as e:
            return {'Exception': str(e)}
        if student:
            return 'Student exists already'
        else:
            parser.add_argument('password', required=True)
            parser.add_argument('name', required=True)
            parser.add_argument('degree', required=True)
            parser.add_argument('cgpa', required=True)
            args2 = parser.parse_args()
            student = Student(args2['username'], args2['password'], args2['name'], args2['degree'], args2['cgpa'])
            try:
                db.session.add(student)
                db.session.commit()
                return 'Student is added successfully'
            except Exception as e:
                return {'exception': str(e)}

    # get all students from database
    def get(self):
        students = Student.query.all()
        students_list_json = [{
            'username': student.username,
            'password': student.password,
            'name': student.name,
            'degree': student.degree,
            'cgpa': student.cgpa
        } for student in students]
        return students_list_json

    # update student
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        args1 = parser.parse_args()
        student = Student.query.get(args1['username'])

        if not student:
            return "Student does not exist"
        else:
            parser.add_argument('password', required=True)
            parser.add_argument('name', required=True)
            parser.add_argument('degree', required=True)
            parser.add_argument('cgpa', required=True)
            args2 = parser.parse_args()

            student.password = args2['password']
            student.name = args2['name']
            student.degree = args2['degree']
            student.cgpa = args2['cgpa']
            try:
                db.session.commit()
                return "Student is updated successfully"
            except Exception as e:
                return {'Exception': str(e)}

    # delete student
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, location='args')  # gets argument from request query string
        args = parser.parse_args()
        student = Student.query.get(args['username'])

        if not student:
            return "Student does not exist"
        else:
            try:
                db.session.delete(student)
                db.session.commit()
                return "Student is deleted successfully"
            except Exception as e:
                return {'Exception': str(e)}
