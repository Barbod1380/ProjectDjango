from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   username = models.CharField(verbose_name="username", max_length=50)
   password = models.CharField(verbose_name="password", max_length=50)
   email = models.CharField(verbose_name="email", max_length=50)
   Student_Number = models.CharField(verbose_name="Student_Number", max_length=50)



class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    student_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.first_name , self.last_name

class Product(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)



