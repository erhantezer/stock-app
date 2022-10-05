from django.urls import path,include
from rest_framework import routers
from .views import (
    CategoryViewListCreate,
    CategoryURD,
    BrandViewSet,
    ProductViewSet,
    FirmViewSet,
    StockViewSet,
)

router = routers.DefaultRouter()
router.register("brand",BrandViewSet)
router.register("product",ProductViewSet)
router.register("firm",FirmViewSet)
router.register("stock",StockViewSet)


urlpatterns =[
    path("category/",CategoryViewListCreate.as_view()),
    path("category/<int:pk>",CategoryURD.as_view()),
    path("",include(router.urls))
     
]
