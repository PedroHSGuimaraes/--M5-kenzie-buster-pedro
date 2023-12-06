from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from .serializers import MovieOrderSerializer, MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import VerifyPermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieOrderSerializer, MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import VerifyPermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [VerifyPermission]

    def get(self, request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [VerifyPermission]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
        except Movie.DoesNotExist:
            return Response(
                {"message": "Filme não encontrado"}, status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie_obj = get_object_or_404(Movie, pk=movie_id)

        # Adicionando movie_id ao request.data para o serializer MovieOrderSerializer
        request.data["movie"] = movie_id

        serializer = MovieOrderSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save(movie=movie_obj, user_order=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
