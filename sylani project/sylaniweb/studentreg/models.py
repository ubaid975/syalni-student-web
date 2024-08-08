from django.db import models
import random

# Create your models here.
class students(models.Model):
    rollno=random.randint(111111,999999)
    city=models.CharField(max_length=100,null=False)
    course=models.CharField(max_length=100,null=False)
    campus=models.CharField(max_length=100,null=False)
    timing=models.CharField(max_length=100,null=False)
    name=models.CharField(max_length=150,null=False)
    fname=models.CharField(max_length=150,null=False)
    email=models.EmailField()
    Phone=models.CharField(max_length=11)
    cnic=models.CharField(max_length=14)
    fcnic=models.CharField(max_length=14)
    dob=models.DateField()
    address=models.CharField(max_length=1000,null=False)
    qulification=models.CharField(max_length=100,null=False)
    laptop=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class campus(models.Model):
    city=models.CharField(max_length=200)
    campus=models.CharField(max_length=200)
    course=models.CharField(max_length=200)
    timing=models.CharField(max_length=200)
    def __str__(self):
        return self.city

