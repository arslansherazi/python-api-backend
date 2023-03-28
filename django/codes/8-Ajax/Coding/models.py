from django.db import models
from marshmallow import Schema, fields


class Student(models.Model):
    roll_no = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    cgpa = models.CharField(max_length=255)

    class Meta:
        db_table = "Student"


class StudentSchema(Schema):
    roll_no = fields.Str()
    name = fields.Str()
    degree = fields.Str()
    cgpa = fields.Str()
