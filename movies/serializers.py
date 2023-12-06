from rest_framework import serializers
from .models import RatingOptions, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=RatingOptions.choices, default=RatingOptions.DEFAULT
    )
    synopsis = serializers.CharField(default=None)

    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        user = validated_data.pop("user")
        return Movie.objects.create(**validated_data, user=user)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(source="movie.title", read_only=True)

    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    bought_at = serializers.DateTimeField(read_only=True)

    bought_by = serializers.CharField(source="user_order.email", read_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
