
from dataclasses import fields
from .models import (
    Category,
    Brand,
    Stock,
    Firm,
    Product,
)
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"
        
class ProductSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields=(
            "id",
            "product_name",
            "category",
            "brand",
            "stock_quantity",
        )
        read_only_fields = ('stock_quantity',) #!sadece okusun biz işlemi zaten signalsta yaptık
        
class FirmSerializers(serializers.ModelSerializer):
    class Meta:
        model=Firm
        fields=(
            "id",
            "firm_name",
            "phone_number",
            "adsress",
        )
        
class StockSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    firm=serializers.StringRelatedField()
    user_id=serializers.IntegerField(write_only=True)
    firm_id=serializers.IntegerField(write_only=True)
    product_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Stock
        fields=(
            "id",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "transaction",
            "product",
            "product_id",
            "quentity",
            "price",
            "price_total",
        )
        read_only_fields = ('price_total',) #!sadece okusun biz işlemi zaten signalsta yaptık
        
    def validate(self, data):
        if data.get('transaction') == 0:
            product = Product.objects.get(id=data.get('product_id'))
            if data.get('quantity') > product.stock:
                raise serializers.ValidationError(
                    f'Dont have enough stock. Current stock is {product.stock}'
                )
        return data