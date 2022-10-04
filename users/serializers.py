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