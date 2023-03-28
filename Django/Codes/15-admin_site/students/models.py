from django.db import models


class Student(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    cgpa = models.FloatField()

    class Meta:
        db_table = 'student'


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester_no = models.IntegerField()
    gpa = models.FloatField()

    class Meta:
        db_table = 'semester'
