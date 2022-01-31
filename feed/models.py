from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    id = models.CharField(primary_key=True, max_length=200)

    place_name = models.CharField(max_length=200)
    place_url = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    category_name = models.CharField(max_length=200)
    category_group_code = models.CharField(max_length=200)
    category_group_name = models.CharField(max_length=200)

    address_name = models.CharField(max_length=200)
    road_address_name = models.CharField(max_length=200)
    x = models.CharField(max_length=200)
    y = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
