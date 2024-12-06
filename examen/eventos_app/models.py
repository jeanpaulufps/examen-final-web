from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    pub_date = models.DateField()
    location = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

