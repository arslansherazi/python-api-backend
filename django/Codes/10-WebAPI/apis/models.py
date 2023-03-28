from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    cgpa = models.FloatField()

    class Meta:
        db_table = "Student"

