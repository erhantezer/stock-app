<font color="green"><h1 style="text-align:center">STOCK APP</h1></font>

<font color="red"> 
Önce users authenticate işlemlerini serializers da register serializers işlemini opsiyonel olarak custom token serializer ve user token serializer işlemlerini rest apide usera girdiğim verileri görmek için yaptık ve view kısmını yaptık  view de register işlemini ve token eklemeyi yaptık ve signals.py de register olunca token üretmek işini yaptık ardından  istersek permissions.py açarak burda 

```python
class CustomModelPermission(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
```
CRUD işlemleri için istersek nelere izin verebileceğimizi ekstra yaptık özellikle get view işlemini ekledik, rest auth işemini urls e ekledik ayrıca özelleştirdiğimiz register işlemi için endpoint oluşturduk . Ardından Stock app e geçerek model işlemlerini 

</font>

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
source env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
pip install dj-rest-auth 
pip install django-filter
pip install djangorestframework
pip install drf-yasg
pip install python-decouple
pip install requests

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install djangorestframework
pip freeze > requirements.txt

# alternatively python -m pip install django
pip install python-decouple
django-admin --version
```

1-python -m venv env
2-source env/Scripts/activate
django-admin startproject main .
3-pip install -r requirements.txt 🚀
4-python.exe -m pip install --upgrade pip
5-python manage.py migrate
6-python manage.py createsuperuser
7-python manage.py runserver



```
## 🛑 Secure your project

## 🚩 .gitignore

✔ Add a ".gitignore" file at same level as env folder, and check that it includes ".env" and /env lines.

🔹 Do that before adding your files to staging area, else you will need extra work to unstage files to be able to ignore them.

🔹 [On this page](https://www.toptal.com/developers/gitignore) you can create "gitignore files" for your projects.

## 🚩 Python Decouple

💻 To use python decouple in this project, first install it 👇

```bash
pip install python-decouple
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

✔ Create a new file and name as ".env" at same level as env folder

✔ Copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks and blanks from SECRET_KEY

```python
SECRET_KEY=-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

✔ Go to "settings.py", make amendments below 👇

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

## 💻 INSTALLING DJANGO REST

💻 Go to terminal 👇

```bash
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
```

✔ Go to "settings.py" and add 'rest_framework' app to INSTALLED_APPS

## 💻 PostgreSQL Setup

💻 To get Python working with Postgres, you will need to install the “psycopg2” module👇

```bash
pip install psycopg2
```

💻 Go to terminal to update requirements.txt  👇

```bash
pip freeze > requirements.txt
```

✔ Go to settings.py and add '' app to INSTALLED_APPS

## 💻 MIGRATE 👇

```bash
python manage.py migrate
```

## 🚀 RUNSERVER 👇

```bash
python manage.py runserver
```

# <center> ✏ This is the end of initial setup ✏ </center>

## <center> ****************************************************** </center>

# <center> 🚀 AUTHENTICATION </center>

## 🚩 ADDING AN APP

💻 Go to terminal 👇

```bash
python manage.py startapp users
```

✔ Go to "settings.py" and add 'account' App to "INSTALLED_APPS"

## 💻 INSTALL [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/)

```bash
pip install dj-rest-auth
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

## 🚩 Add "dj_rest_auth" app to "INSTALLED_APPS" in your django "settings.py" 👇

```python
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
```

## 🚩 Go to "main/urls.py" and add the path 👇

```python
path('users/', include('users.urls'))
```

## ✔ Create "urls.py" file under "account" App 👇

## 🚩 Go to "account/urls.py" and add 👇

```python
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

## 💻 Migrate your database

```bash
python manage.py migrate
```
## ✔ Create "serializers.py" file under "users" App and add 👇
```python
from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializers(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(
        write_only=True,
         required=True,
         validators=[validate_password],
         style={"input_type" :"password"}
    )
    password1=serializers.CharField(
        write_only=True,
         required=True,
         validators=[validate_password],
         style={"input_type" :"password"}
    )
    class Meta:
        model=User
        fields=(
            "username",
            "email",
            "password",
            "password1",
            "first_name",
            "last_name"
        )
    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValueError(
                {"password": "Password didn't match .. "}
            )
        return data

    def create(self, validate_data):
        password=validate_data.pop("password")
        validate_data.pop("password1")
        user=User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        return user


```
## 🚩 Go to "views.py" and write RegisterVİew() 👇
```py
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_expeption=True)
        user=serializer.save()
        data=serializer.data
        
        if Token.objects.filter(user=user).exists():
            token=Token.objects.get(user=user)
            data["token"] = token.key
            
        else:
            data["token"] = "No token created for this user.... :))"
            headers = self.get_success_headers(serializer.data)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```
## 🚩 Go to "urls.py" and add the path 👇

```python
from .views import RegisterView

path('register/', RegisterView.as_view()),
```

## 🚩 Create "signals.py" under "users" App and add 👇

```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

## 🚩 For the "signal.py" file to work, we need to add the "ready" method to the "apps.py" file 👇

```python
def ready(self) -> None:
    import users.signals
	```
	## 🚩 Override TokenSerializer() 👇

```python
from dj_rest_auth.serializers import TokenSerializer

#! We need to override the TokenSerializer to return all user data in a single request.
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class CustomTokenSerializer(TokenSerializer):

    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
```
## 🚩 Go to "settings.py" and add 👇

```python
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'account.serializers.CustomTokenSerializer',
}
```

## <center> ****************************************************** </center>
## 🚩 ADDING APP

💻 Go to terminal 👇

```bash
python manage.py startapp stock
```

✔ Go to "settings.py" and add 'stock' App to "INSTALLED_APPS"

## 🚩 Go to "main/urls.py" and add path 👇

```python
 path('stock/', include('stock.urls')),
```
## 🚩 Go to "models.py" under "stock" App and create models 👇

```python
from itertools import product
from random import choices
from django.db import models
from django.contrib.auth.models import User

class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(UpdateCreate):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='b_products')
    stock = models.SmallIntegerField(blank=True, null=True)
    #! We used SmallIntegerField to take up less space in the database 👆

    def __str__(self):
        return self.name

class Firm(UpdateCreate):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Transaction(UpdateCreate):
    TRANSACTIONS = (
        ("1", "IN"),
        ("0", "OUT"),
    )
    #! When you say SET_NULL, it is necessary to write "null=True". When the user is deleted, that field in db will remain null 👇
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name='transactions')
    transaction = models.SmallIntegerField(choices=TRANSACTIONS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='transaction')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.transaction} - {self.product} - {self.quantity}'
```

# 💻 Migrate your database 👇

```bash
python manage.py migrate
```

## 🚩 Go to "admin.py" and register the models 👇

```python
from django.contrib import admin

from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Transaction)
```
## 🚩 Create "serializers" file under "stock" App and add 👇
```py

from dataclasses import fields
from .models import (
    Category,
    Brand,
    Transaction,
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
            "stock",
        )
        read_only_fields = ('stock',) #!sadece okusun biz işlemi zaten signalsta yaptık
        
class FirmSerializers(serializers.ModelSerializer):
    class Meta:
        model=Firm
        fields=(
            "id",
            "firm_name",
            "phone_number",
            "address",
        )
        
class StockSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    product=serializers.StringRelatedField()
    firm=serializers.StringRelatedField()
    user_id=serializers.IntegerField(write_only=True)
    firm_id=serializers.IntegerField(write_only=True)
    product_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Transaction
        fields=(
            "id",
            "user",
            "user_id",
            "firm",
            "firm_id",
            "transaction",
            "product",
            "product_id",
            "quantity",
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
```
## 🚩 Create  "signals.py" file under "stock" App and add 👇

```python
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Transaction, Product

#! We are doing database related operations here, so we can return the warning message from serializers.

@receiver(pre_save, sender=Transaction)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantity * instance.price

@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product_id)
    if instance.transaction == 1:
        if not product.stock:
            #! first came as null so we did it like this 👆
            product.stock = instance.quantity
        else:
           product.stock += instance.quantity
    else:
        product.stock -= instance.quantity

    product.save()
```

## 🚩 For the "signal.py" file to work, we need to add the "ready" method to the "apps.py" file 👇

```python
    def ready(self):
        import stock.signals
```

## 🚩 Go to "views.py" and start to write views 👇

```py
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
```
## 🚩 Create "urls.py" file under "stock" App and add 👇
```py
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
```