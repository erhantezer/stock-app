from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializers
from rest_framework.authtoken.models import Token

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


