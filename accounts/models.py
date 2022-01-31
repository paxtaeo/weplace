from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    screen_name = models.CharField(max_length=150, blank=True)

    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')

    def follow(self, username):
        other = User.objects.get(username=username)
        self.following.add(other)
    
    def unfollow(self, username):
        other = User.objects.get(username=username)
        self.following.remove(other)
