from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    student_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.first_name , self.last_name

class Product(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)

class Order(models.Model):
    #customer =
    #product =
    name = models.CharField(max_length=50, null=True)

