from django.shortcuts import render
from .serializers import (
    CategorySerializers,
    )

from .models import (
    Category,
    Firm,
    Brand,
    Product,
    Stock
)
from rest_framework import generics


class CategoryViewListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
