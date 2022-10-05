from django.contrib import admin

from stock.models import (
    Brand, 
    Category, 
    Firm, 
    Product, 
    Stock
    )

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Brand)
admin.site.register(Stock)