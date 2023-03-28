from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=100)
    current_semester = models.IntegerField()
    session_start = models.CharField(max_length=50)
    session_end = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student'
        app_label = 'apis'


class StudentProfile(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contact_no = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_profile'
        app_label = 'apis'

    @classmethod
    def add_student_profile(cls, student_id, first_name, last_name, address, contact_no, **kwargs):
        """
        Adds student profile
        """
        student_profile = cls(
            student_id=student_id, first_name=first_name, last_name=last_name, address=address, contact_no=contact_no
        )
        student_profile.save()
