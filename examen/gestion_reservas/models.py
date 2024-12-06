from django.db import models

# Create your models here.

class Table(models.Model):
    tale_number = models.SmallIntegerField(unique=True)
    capacity = models.SmallIntegerField()
    isAvailable = models.BooleanField(default=True)

class Reservation(models.Model):
    client = models.CharField(max_length=120)
    res_date = models.DateField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

