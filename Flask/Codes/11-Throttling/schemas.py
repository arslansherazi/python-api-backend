from models import *
from app import mm


class CompanySchema(mm.ModelSchema):
    class Meta:
        model = Company