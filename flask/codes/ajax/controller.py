from flask import render_template, request, jsonify
import json

from app import app, db
from models import Student
from schemas import StudentSchema


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/no_js')
def no_js():
    return render_template('no_js.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    roll_no = request.form['roll_no']
    name = request.form['name']
    degree = request.form['degree']
    cgpa = request.form['cgpa']

    student = Student(roll_no=roll_no, name=name, degree=degree, cgpa=cgpa)
    try:
        db.session.add(student)
        db.session.commit()
        return 'Student is added successfully'
    except Exception as e:
        return str(e)


@app.route('/get_all_students')
def get_all_students():
    try:
        students = Student.query.all()
        if students:
            student_schema = StudentSchema(many=True)
            students_response = student_schema.dump(students).data
            students_json_response = jsonify(students_response)
            return json.dumps(students_json_response.json)
        else:
            return 'no students in the database yet'
    except Exception as e:
        return str(e)


@app.route('/search_student')
def search_student():
    roll_no = request.args['roll_no']
    try:
        student = Student.query.get(roll_no)
        if student:
            student_schema = StudentSchema()
            student_response = student_schema.dump(student).data
            student_json_response = jsonify(student_response)
            return json.dumps(student_json_response.json)
        else:
            return 'no student found'
    except Exception as e:
        return str(e)


@app.route('/delete_student')
def delete_student():
    roll_no = request.args['roll_no']
    try:
        student = Student.query.get(roll_no)
        db.session.delete(student)
        db.session.commit()
        return 'Student is deleted successfully'
    except Exception as e:
        return str(e)


@app.route('/update_student', methods=['POST'])
def update_student():
    roll_no = request.form['roll_no']
    name = request.form['name']
    degree = request.form['degree']
    cgpa = request.form['cgpa']
    try:
        student = Student.query.get(roll_no)
        student.name = name
        student.degree = degree
        student.cgpa = cgpa
        db.session.commit()
        return 'Student is updated successfully'
    except Exception as e:
        return str(e)
