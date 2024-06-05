from django.db import models
from django.contrib.auth.models import AbstractUser  
from rest_framework.viewsets import ModelViewSet


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300,default='username')
    phone_no = models.CharField(max_length=300)
    address = models.CharField(max_length=300)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_no','address']

    # email = admin@gmail.com
    # password = 12345sss
    # username =admin



class productCategory(models.Model):
    name = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.IntegerField()

class product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    stock = models.IntegerField()
    category = models.ForeignKey(productCategory,on_delete=models.SET_NULL,null=True)
    Department = models.ManyToManyField(Department, null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    contact = models.IntegerField()
    address = models.CharField(max_length=300)
    email = models.EmailField()

class Purchase(models.Model):
    quantity = models.IntegerField()
    price = models.IntegerField()
    product = models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)
