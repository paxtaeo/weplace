from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from accounts.models import User
from .models import Restaurant, Review

class Profile(generic.DetailView):
    template_name = 'feed/profile.html'
    context_object_name = 'user'

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return user

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        context = super().get_context_data(**kwargs)
        context['reviews'] = user.reviews.all()
        return context
