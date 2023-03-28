from django.db import models

# Create your models here.
class Reservations(models.Model):
    Username = models.CharField(max_length=255)
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    Departure = models.CharField(max_length=255)
    Arrival = models.CharField(max_length=255)
    Seats = models.CharField(max_length=255)

    class Meta:
        db_table = "Reservations"