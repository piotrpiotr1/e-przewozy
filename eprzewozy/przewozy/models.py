from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name_patron = models.CharField(max_length=50)
    last_name_patron = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    school_address = models.CharField(max_length=50)
    home_address = models.CharField(max_length=50)
    task = models.CharField(max_length=10)