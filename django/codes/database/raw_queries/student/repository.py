from student.models import Student
from student.serializers.student_serializer import StudentSerializer
from django.db import connection


class StudentRepository:
    def add_student(self, username, name, degree, cgpa):
        query = '''
            INSERT INTO student(username, name, degree, cgpa)
            VALUES(%s, %s, %s, %s)
        '''
        params = [username, name, degree, cgpa]
        try:
            Student.objects.raw(query, params)
            return True
        except Exception:
            return False

    def delete_student(self, username):
        query = '''
            DELETE FROM student
            WHERE username = %s
        '''
        params = [username]
        try:
            Student.objects.raw(query, params)
            return True
        except Exception:
            return False

    def get_all_students(self):
        query = '''
            SELECT *
            FROM student s
        '''
        result = Student.objects.raw(query)
        students = []
        if result:
            for student_obj in result:
                student = StudentSerializer(student_obj).data
                students.append(student)
        return students

    def get_particular_student(self, username):
        query = '''
            SELECT *
            FROM student
            WHERE username = %s
        '''
        params = [username]

        #result = Student.objects.raw(query, params)
        #if result:
        #   student = StudentSerializer(result[0]).data
        #return student

        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        columns = [col[0] for col in cursor.description]
        student = dict(zip(columns, result))
        return student

    def get_particular_student_by_degree_and_cgpa(self, degree, cgpa):
        query = '''
            SELECT username, name
            FROM student
            WHERE degree = %s
            AND cgpa = %s
        '''
        params = [degree, cgpa]
        cursor = connection.cursor()
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result

    def update_student(self, username, name, degree, cgpa):
        query = '''
            UPDATE student
            SET name = %s
            AND degree = %s
            AND cgpa = %s
            WHERE username = %s
        '''
        params = [username, name, degree, cgpa]
        try:
            Student.objects.raw(query, params)
            return True
        except Exception:
            return False