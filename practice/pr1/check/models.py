from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100,default=None)
    mobile = models.IntegerField()



class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

