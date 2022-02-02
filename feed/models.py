from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    id = models.CharField(primary_key=True, max_length=200)

    place_name = models.CharField(max_length=200)
    place_url = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)

    category_name = models.CharField(max_length=200, blank=True)
    category_group_name = models.CharField(max_length=200, blank=True)
    category_group_code = models.CharField(max_length=200, blank=True)

    address_name = models.CharField(max_length=200, blank=True)
    road_address_name = models.CharField(max_length=200, blank=True)
    x = models.CharField(max_length=200)
    y = models.CharField(max_length=200)

    @property
    def num_reviews(self):
        return self.reviews.count()

    @property
    def rating(self):
        ratings = [review.rating for review in self.reviews.all()]
        return round(sum(ratings)/len(ratings), 2) if len(ratings) != 0 else '-'

    def __str__(self):
        return self.place_name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')

    one_to_ten_choices = [(i, i) for i in range(1,11)]
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], choices=one_to_ten_choices)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('feed:user_profile', kwargs={'username': self.user.username})


# for field in ['id', 'place_name', 'place_url', 'phone', 'category_name', 'category_group_name', 'category_group_code', 'address_name', 'road_address_name', 'x', 'y']:
#     print(f"{field}=self.request.POST['{field}']")
#     print(f'<input id="input_{field}" name="{field}" hidden>')
