import json

from flask_restful import Resource, reqparse

from flask_mongo_db_crud.student_model import Student, SemesterDetails, Semesters


class StudentApis(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('roll_no', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('degree', type=str, required=True)
        parser.add_argument('cgpa', type=float, required=True)
        parser.add_argument('semesters_details', type=dict, required=True)
        args = parser.parse_args()
        try:
            roll_no = args.get('roll_no')
            name = args.get('name')
            degree = args.get('degree')
            cgpa = args.get('cgpa')
            semesters_deatils = args.get('semesters_details')
            student = Student(roll_no=roll_no, name=name, degree=degree, cgpa=cgpa, semesters_details=semesters_deatils)
            student.save()
            return {
                'status_code': 200,
                'success': True,
                'message': 'Student is added successfully'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('roll_no', type=str, required=True)
        args = parser.parse_args()
        try:
            roll_no = args.get('roll_no')
            student = Student.objects(roll_no=roll_no)
            if student:
                return {
                    'status_code': 200,
                    'success': True,
                    'data': student.first().to_dict()
                }
            else:
                return {
                    'status_code': 200,
                    'success': True,
                    'message': 'No student is found'
                }
        except Exception as e:
            return {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('roll_no', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('degree', type=str, required=True)
        parser.add_argument('cgpa', type=float, required=True)
        parser.add_argument('semesters_details', type=dict, required=True)
        args = parser.parse_args()
        try:
            roll_no = args.get('roll_no')
            name = args.get('name')
            degree = args.get('degree')
            cgpa = args.get('cgpa')
            semesters_deatils = args.get('semesters_details')
            student = Student.objects(roll_no=roll_no)
            student.name = name
            student.degree = degree
            student.cgpa = cgpa
            semesters_details = []
            for semester_name in semesters_deatils.keys():
                gpa = semesters_deatils.get(semester_name).get('gpa')
                major_subjects = semesters_deatils.get(semester_name).get('major_subjects')
                semester_detail = SemesterDetails(gpa=gpa, major_subjects=major_subjects)
                semesters_details.append(semester_detail)
            semesters = Semesters()
            semesters.semester1 = semesters_details[0]
            semesters.semester2 = semesters_details[1]
            semesters.semester3 = semesters_details[2]
            semesters.semester4 = semesters_details[3]
            semesters.semester5 = semesters_details[4]
            semesters.semester6 = semesters_details[5]
            semesters.semester7 = semesters_details[6]
            semesters.semester8 = semesters_details[7]
            student.semesters_details = semesters
            student.save()
            return {
                'status_code': 200,
                'success': True,
                'message': 'Student is updated successfully'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('roll_no', type=str, required=True)
        args = parser.parse_args()
        try:
            roll_no = args.get('roll_no')
            student = Student.objects(roll_no=roll_no)
            if student:
                student.delete()
                return {
                    'status_code': 200,
                    'success': True,
                    'message': 'Student is deleted successfully'
                }
            else:
                return {
                    'status_code': 200,
                    'success': True,
                    'message': 'Student does not exist'
                }
        except Exception as e:
            return {
                'status_code': 500,
                'success': False,
                'message': 'Internal Server Error',
                'exception': str(e)
            }
