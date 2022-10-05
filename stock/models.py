from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    brand = models.ForeignKey(Brand, on_delete=CASCADE)
    stock = models.IntegerField()
    
    
class Firm(models.Model):
    firm_name = models.CharField(max_length=50) 
    phone_number = models.IntegerField()   
    address = models.CharField(max_length=50)
    
    
class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    firm = models.ForeignKey(Firm, on_delete=CASCADE)
    transaction = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=CASCADE)

