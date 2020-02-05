from sqlalchemy import text

from app import db


class StudentRepository:
    def add_student(self, username, name, degree, cgpa):
        query = '''
            INSERT INTO student(username, name, degree, cgpa)
            VALUES(:username, :name, :degree, :cgpa)
        '''
        params = {
            'username': username,
            'name': name,
            'degree': degree,
            'cgpa': cgpa
        }
        try:
            db.engine.execute(text(query), params)
            return True
        except Exception:
            return False

    def delete_student(self, username):
        query = '''
            DELETE FROM student
            WHERE username = :username
        '''
        params = {'username': username}
        try:
            db.engine.execute(text(query), params)
            return True
        except Exception:
            return False

    def get_all_students(self):
        query = '''
            SELECT *
            FROM student
        '''
        result = db.engine.execute(text(query)).fetchall()
        students = []
        for row in result:
            student = dict(row.items())
            students.append(student)
        return students

    def get_particular_student(self, username):
        query = '''
            SELECT *
            FROM student
            WHERE username = :username
        '''
        params = {'username': username}
        result = db.engine.execute(text(query), params).fetchone()
        student = dict(result.items())
        return student

    def update_student(self, username, name, degree, cgpa):
        query = '''
            UPDATE student
            SET name = :name,
            degree = :degree,
            cgpa = :cgpa
            WHERE username = :username
        '''
        params = {
            'username': username,
            'name': name,
            'degree': degree,
            'cgpa': cgpa
        }
        try:
            db.engine.execute(text(query), params)
            return True
        except Exception as e:
            return False
 