from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )

    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )

    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    password = serializers.CharField(max_length=127, write_only=True)

    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        try:
            if validated_data["is_employee"] == True:
                return User.objects.create_superuser(**validated_data)
            else:
                return User.objects.create_user(**validated_data)
        except KeyError:
            return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        try:
            instance.set_password(validated_data["password"])
            instance.save()
        except KeyError:
            pass

        instance.save()

        return instance
