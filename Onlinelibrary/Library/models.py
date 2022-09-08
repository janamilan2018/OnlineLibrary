from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20, default='')
    def __str__(self):
        return str(self.id)

class PDF(models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="PDF_File/")

