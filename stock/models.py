from django.db import models
from django.contrib.auth.models import User

#! Eğer farklı modellerde aynı yapıda field kullanmak istiyorsak abstract class tanımlaması yaparak
#! inherit edebiliriz.Tüm classlarda name field kullanılcaksa 
"""
class NameCreated(models.Model) :
    name =models.CharField(max_length=50)
    class Meta:
        abstract =True
     # Kullanılacak classta
     class Category (NameCreated)  :
        #? name field inherit edildiğinden gelecek. 
"""

class Category(models.Model):
   category_name=models.CharField(max_length=50)

   def __str__(self):
       return self.category_name
   class Meta:
      verbose_name_plural="Categories"



class Brand(models.Model):
     brand_name=models.CharField(max_length=50)

     def __str__(self):
       return self.brand_name


class Product(models.Model):
    product_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock=models.IntegerField()

    def __str__(self):
       return f"{self.brand} - {self.product_name} - Stok miktarı :  {self.stock}"



class Firm(models.Model):
    firm_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address =models.CharField(max_length=50)

    def __str__(self):
       return f"{self.firm_name}"


class Transaction(models.Model):
    TRANSACTION = (
        (1, 'IN'),
        (0, 'OUT')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(
        Firm, on_delete=models.SET_NULL, null=True, related_name='transactions')
    transaction = models.SmallIntegerField(choices=TRANSACTION)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='transaction')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.transaction} - {self.product} - {self.quantity}'