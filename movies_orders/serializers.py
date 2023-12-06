from rest_framework import serializers
from .models import MovieOrder
from movies.serializers import MovieSerializer
from django.contrib.auth.models import User


class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    purchased_by = serializers.SerializerMethodField()

    class Meta:
        model = MovieOrder
        fields = ["id", "title", "purchased_at", "price", "purchased_by"]

    def get_title(self, obj):
        return obj.movie.title

    def get_purchased_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = self.context["request"].user
        movie = validated_data["movie"]
        price = validated_data["price"]
        return MovieOrder.objects.create(user=user, movie=movie, price=price)
