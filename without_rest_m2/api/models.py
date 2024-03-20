from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    gf = models.CharField(max_length=20)
    bf = models.CharField(max_length=20)