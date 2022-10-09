from rest_framework.permissions import (
    # IsAuthenticated, 
    DjangoModelPermissionsOrAnonReadOnly
    )

from django_filters.rest_framework import DjangoFilterBackend

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
    Transaction
)
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import  filters

class CategoryViewListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
class CategoryURD(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
class StockViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = StockSerializers
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['firm', 'transaction', 'product']
    search_fields = ['firm']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)