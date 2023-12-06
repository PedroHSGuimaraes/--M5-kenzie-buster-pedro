from django.db import models

class RatingOptions(models.TextChoices):
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"
    DEFAULT = "G"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=RatingOptions.choices, default=RatingOptions.DEFAULT)
    synopsis = models.TextField(null=True, default=None)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")
    
    orders = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="order_movie")
    
class MovieOrder(models.Model):
    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)
    
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name='movie_order')
                              
    user_order = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie_order")
    