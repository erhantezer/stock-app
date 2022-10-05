from django.shortcuts import render
from .serializers import (
    CategorySerializers,
    BrandSerializers
    )

from .models import (
    Category,
    Firm,
    Brand,
    Product,
    Stock
)
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

class CategoryViewListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
class CategoryURD(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers