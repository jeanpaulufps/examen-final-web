from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    archive = models.ImageField()
    pub_date = models.DateField()

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

class DownloadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ForeignKey(Image, on_delete=models.CASCADE)


