from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly
from .serializers import (
    CategorySerializers,
    BrandSerializers,
    ProductSerializers,
    FirmSerializers,
    StockSerializers,
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
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializers
    
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers
    permission_classes=[IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]