from django.db import models
from django.db.models import F


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=100)
    current_semester = models.IntegerField(max_length=50)
    session_start = models.CharField(max_length=50)
    session_end = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student'
        app_label = 'apis'

    @classmethod
    def get_students_profiles(cls):
        """
        Gets students profiles
        """
        query = cls.objects
        query = query.values(
            'id', 'roll_no', 'current_semester', 'session_start', 'session_end',
            first_name=F('studentprofile__first_name')
        )
        students_data = query.all()
        return students_data

    @classmethod
    def insert_student_into_db(cls, roll_no, current_semester, session_start, session_end):
        """
        Inserts student into db
        """
        student = cls(
            roll_no=roll_no, current_semester=current_semester, session_start=session_start, session_end=session_end
        )
        student.save()
        return student.id


class StudentProfile(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    contact_no = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_profile'
        app_label = 'apis'

    @classmethod
    def get_students_profiles(cls):
        """
        Gets students profiles
        """
        students_profiles = cls.objects.all()
        students = []
        for student_profile in students_profiles:
            student = {
                'id': student_profile.student_id,
                'first_name': student_profile.first_name,
                'last_name': student_profile.last_name,
                'address': student_profile.address,
                'contact_no': student_profile.contact_no,
                # new database query is made for following
                'roll_no': student_profile.student.roll_no,
                'current_semester': student_profile.student.current_semester,
                'session_start': student_profile.student.session_start,
                'session_end': student_profile.student.session_end
            }
            students.append(student)
        return students

    @classmethod
    def get_select_related_students_profiles(cls):
        """
        Gets students profiles
        """
        query = cls.objects
        students_profiles = query.select_related('student').all()
        students = []
        for student_profile in students_profiles:
            student = {
                'id': student_profile.student_id,
                'first_name': student_profile.first_name,
                'last_name': student_profile.last_name,
                'address': student_profile.address,
                'contact_no': student_profile.contact_no,
                # new database query is not made for following. data is already fetched using select related
                'roll_no': student_profile.student.roll_no,
                'current_semester': student_profile.student.current_semester,
                'session_start': student_profile.student.session_start,
                'session_end': student_profile.student.session_end
            }
            students.append(student)
        return students

    @classmethod
    def add_student_profile_into_db(cls, student_id, address, first_name, last_name, contact_no):
        """
        Add student profile into db
        """
        student_profile = cls(
            student_id=student_id, address=address, first_name=first_name, last_name=last_name, contact_no=contact_no
        )
        student_profile.save()


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    students = models.ManyToManyField(Student)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course'
        app_label = 'apis'

    @classmethod
    def add_course_into_db(cls, code, name):
        """
        Adds course into db
        """
        course = cls(code=code, name=name)
        course.save()

    @classmethod
    def assign_student_course(cls, course_id, student_id):
        """
        Assigns course to a student
        """
        student = Student.objects.get(id=student_id)
        course = cls.objects.get(id=course_id)
        if student and course:
            course.student.add(student)
            course.save()

    @classmethod
    def get_students_courses(cls):
        """
        Gets students courses
        """
        courses = cls.objects.all()
        courses_data = []
        for course in courses:
            course_data = {
                'code': course.code,
                'name': course.name,
            }
            students_data = []
            # Reverse Foreign Key (RelatedManager)
            students = course.students.all()
            for student in students:
                student_data = {
                    'id': student.id,
                    'roll_no': student.roll_no,
                    # Getting user profile data using RelatedManager (prefetch_related technique)
                    'first_name': student.studentprofile.first_name,
                    'last_name': student.studentprofile.last_name,
                    'contact_no': student.studentprofile.first_name.contact_no,
                    'address': student.studentprofile.first_name.address
                }
                students_data.append(student_data)
            course_data['students'] = students_data
            courses_data.append(course_data)
        return courses_data

    @classmethod
    def get_prefetch_related_students_courses(cls):
        """
        Gets students courses
        """
        # prefetch_related creates RelatedManager for ManyToMany Objects and then use Python joining to associate objects  # noqa: 501
        # courses = cls.objects.select_related('students').all()  # we cannot do this because students is not directly associated with Course model  # noqa: 501
        courses = cls.objects.prefetch_related('students').all()
        courses_data = []
        for course in courses:
            course_data = {
                'code': course.code,
                'name': course.name,
            }
            students_data = []
            # Reverse Foreign Key (RelatedManager)
            students = course.students.all()
            for student in students:
                student_data = {
                    'id': student.id,
                    'roll_no': student.roll_no,
                    # Getting user profile data using RelatedManager (prefetch_related technique)
                    'first_name': student.studentprofile.first_name,
                    'last_name': student.studentprofile.last_name,
                    'contact_no': student.studentprofile.first_name.contact_no,
                    'address': student.studentprofile.first_name.address
                }
                students_data.append(student_data)
            course_data['students'] = students_data
            courses_data.append(course_data)
        return courses_data
