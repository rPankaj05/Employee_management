from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=50)

 

class Feedback(models.Model):
    name  = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    desc  = models.TextField()
    date  = models.DateTimeField()

