from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)
    email = models.EmailField(unique=True, max_length=127)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)