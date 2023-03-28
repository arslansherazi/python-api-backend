from models import *
from app import mm


class StudentSchema(mm.ModelSchema):
    class Meta:
        model = Student
