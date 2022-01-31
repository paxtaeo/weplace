from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    screen_name = models.CharField(max_length=150, blank=True)

