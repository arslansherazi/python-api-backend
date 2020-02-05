import datetime

from flask import jsonify, json
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
    jwt_refresh_token_required)

from models import *
from app import app
from schemas import StudentSchema


# function based api
@app.route('/api/get_student', methods=['GET'])
@jwt_required
def get_student():  # get details of particular student
    username = get_jwt_identity()  # get username from jwt token
    try:
        student = Student.query.get(username)
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
    # register new student
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
                jwt_access_token = create_access_token(
                    identity=args2['username'],
                    expires_delta=datetime.timedelta(minutes=5)  # expires_delta = False will disable expiration time of token  # Noqa: 501
                )
                jwt_refresh_token = create_refresh_token(
                    identity=args2['username'],
                    expires_delta=datetime.timedelta(days=1)
                )
                data = {
                    "message": "student is added successfully",
                    "jwt_access_token": jwt_access_token,
                    "jwt_refresh_token": jwt_refresh_token
                }
                response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                )
                return response
            except Exception as e:
                return {'exception': str(e)}

    # get all students from database
    @jwt_required
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
    @jwt_required
    def put(self):
        username = get_jwt_identity()   # get username from jwt token
        try:
            student = Student.query.get(username)
        except Exception as e:
            return {'Exception': str(e)}
        if not student:
            return "Student does not exist"
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('password', required=True)
            parser.add_argument('name', required=True)
            parser.add_argument('degree', required=True)
            parser.add_argument('cgpa', required=True)
            args = parser.parse_args()

            student.password = args['password']
            student.name = args['name']
            student.degree = args['degree']
            student.cgpa = args['cgpa']
            try:
                db.session.commit()
                return "Student is updated successfully"
            except Exception as e:
                return {'Exception': str(e)}

    # delete student
    @jwt_required
    def delete(self):
        username = get_jwt_identity()  # get username from jwt token
        try:
            student = Student.query.get(username)
        except Exception as e:
            return {'Exception': str(e)}
        if not student:
            return "Student does not exist"
        else:
            try:
                db.session.delete(student)
                db.session.commit()
                return "Student is deleted successfully"
            except Exception as e:
                return {'Exception': str(e)}


# get new access token when it expired
class RefreshToken(Resource):
    @jwt_refresh_token_required
    def get(self):
        username = get_jwt_identity()
        jwt_access_token = create_access_token(username)
        return {'jwt_access_token': jwt_access_token}


# get new access token and refresh token when refresh token expired
class GenerateToken(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        try:
            student = Student.query.filter_by(username=args['username'], password=args['password']).first()
        except Exception as e:
            return {'Exception': str(e)}
        if not student:
            return 'Wrong credentials. Check username or password'
        else:
            jwt_access_token = create_access_token(
                identity=args['username'],
                expires_delta=datetime.timedelta(minutes=5)
            )
            jwt_refresh_token = create_refresh_token(
                identity=args['username'],
                expires_delta=datetime.timedelta(days=1)
            )
            data = {
                "jwt_access_token": jwt_access_token,
                "jwt_refresh_token": jwt_refresh_token
            }
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            return response
