from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from accounts.models import User
from .models import Place, Review


class UserProfile(generic.DetailView):
    template_name = 'feed/user_profile.html'
    context_object_name = 'profile_owner'

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return user

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        context = super().get_context_data(**kwargs)
        context['review_list'] = user.reviews.all().order_by('-updated_at')
        context['following_list'] = [] if self.request.user.is_anonymous else self.request.user.following.all()
        return context


class PlaceProfile(generic.DetailView):
    template_name = 'feed/place_profile.html'
    context_object_name = 'place'

    def get_object(self):
        place = get_object_or_404(Place, id=self.kwargs.get("id"))
        return place

    def get_context_data(self, **kwargs):
        place = get_object_or_404(Place, id=self.kwargs.get("id"))
        user = self.request.user
        following_list = list(user.following.all())
        following_list.append(user)

        context = super().get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(user__in=following_list, place=place).order_by('-updated_at')
        return context  


class Explore(LoginRequiredMixin, generic.ListView):
    template_name = 'feed/explore.html'
    context_object_name = 'review_list'

    def get_queryset(self):
        user = self.request.user
        following_list = user.following.all()

        return Review.objects.filter(user__in=following_list).order_by('-updated_at')[:100]


@login_required
def follow(request, username):
    request.user.follow(username)
    return redirect('feed:user_profile', username)

@login_required
def unfollow(request, username):
    request.user.unfollow(username)
    return redirect('feed:user_profile', username)


class ReviewCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = Review
    fields = ['place', 'rating', 'comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
