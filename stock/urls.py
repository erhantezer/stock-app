from django.urls import path
from views import (
    CategoryViewListCreate
)


urlpatterns = [
    path("category/",CategoryViewListCreate.as_view()),
]
