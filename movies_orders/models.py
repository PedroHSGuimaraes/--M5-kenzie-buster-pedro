from django.db import models

# Create your models here.
from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.movie.title} by {self.user.email}"
