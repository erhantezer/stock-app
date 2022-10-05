
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str_(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "Categories"

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    def __str_(self):
        return self.brand_name
    

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    
    def __str_(self):
        return f"{self.brand} {self.brand_name} Stock Miktarı : {self.stock_quantity} tanedir"
    
    
    
class Firm(models.Model):
    firm_name = models.CharField(max_length=50) 
    phone_number = models.IntegerField()   
    address = models.CharField(max_length=50)
    
    def __str_(self):
        return f"{self.brand_name}"
    
    
class Stock(models.Model):
    TRANSACTION_TYPE = [
        ("I","IN"),
        ("O","ON"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    transaction = models.CharField(max_length=2, choices=TRANSACTION_TYPE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_product_date = models.DateTimeField(auto_now=True)
    remove_product_date = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_total = models.CharField(max_length=15,)

    def __str_(self):
        return f"{self.product} {self.user} tarafından {self.transaction} işlemi yapıldı"