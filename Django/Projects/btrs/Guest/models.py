from django.db import models

class User(models.Model):
        Username=models.CharField(max_length=255)
        Password=models.CharField(max_length=255)
        Name = models.CharField(max_length=255)
        Email = models.CharField(max_length=255)
        Contact = models.CharField(max_length=255)
        Province = models.CharField(max_length=255)
        City = models.CharField(max_length=255)
        Age = models.CharField(max_length=255)
        Gender = models.CharField(max_length=255)
        Address = models.CharField(max_length=255)

        class Meta:#used to set table name in database.If it is not set then tableName=AppName_modelName.Example Guest_user
                db_table="User"

class Friend(models.Model):
        Name = models.CharField(max_length=255)
        Email = models.CharField(max_length=255)
        FName = models.CharField(max_length=255)
        FEmail = models.CharField(max_length=255)
        Comments=models.CharField(max_length=255)

        class Meta:
                db_table = "Friend"


class Feedbacks(models.Model):
        Name = models.CharField(max_length=255)
        Email = models.CharField(max_length=255)
        Contact = models.CharField(max_length=255)
        Age = models.CharField(max_length=255)
        Gender = models.CharField(max_length=255)
        Feedback = models.CharField(max_length=255)

        class Meta:
                db_table = "Feedbacks"


class Schedule(models.Model):
        From = models.CharField(max_length=255)
        To = models.CharField(max_length=255)
        Date = models.CharField(max_length=255)
        Departure = models.CharField(max_length=255)
        Arrival = models.CharField(max_length=255)
        Status = models.CharField(max_length=255)

        class Meta:
                db_table = "Schedule"


class Fares(models.Model):
        From = models.CharField(max_length=255)
        To = models.CharField(max_length=255)
        Fare = models.CharField(max_length=255)

        class Meta:
                db_table = "Fares"


class Admin(models.Model):
        Username = models.CharField(max_length=255)
        Password = models.CharField(max_length=255)

        class Meta:
                db_table = "Admin"