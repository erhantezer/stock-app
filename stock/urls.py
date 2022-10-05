from django.urls import path,include
from rest_framework import routers
from views import (
    CategoryViewListCreate,
    BrandViewSet,
)

router = routers.DefaultRouter()
router("brand",BrandViewSet)

urlpatterns = [
    path("category/",CategoryViewListCreate.as_view()),
    path("", include(router.urls))
]
