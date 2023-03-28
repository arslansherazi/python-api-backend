from django.db import models

class Book(models.Model):
    id     = models.CharField(max_length = 255, primary_key = True)
    name   = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    price  = models.IntegerField()

    objects = models.Manager()

    class Meta:#Meta is case sensitive => meta != Meta
        #used to set table name in database.If it is not set then TableName=AppName_ModelName.Example Coding_Book
        db_table = 'Book'
