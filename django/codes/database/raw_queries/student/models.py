from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    cgpa = models.FloatField()

    class Meta:
        db_table = 'student'
