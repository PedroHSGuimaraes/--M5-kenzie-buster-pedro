from django.urls import path
from . import views
from .views import MovieDetailView, MovieOrderDetailView

urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
    path(
        "movies/<int:movie_id>/orders/",
        MovieOrderDetailView.as_view(),
        name="movie-order-detail",
    ),
]
