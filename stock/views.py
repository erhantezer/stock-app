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


class CategoryView(generics.ListCreateAPIView):
