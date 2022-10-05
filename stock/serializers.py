
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
