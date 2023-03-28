from django.db import models


class Company(models.Model):
    username = models.CharField(max_length=255, primary_key=True,)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    subscription = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'company'
