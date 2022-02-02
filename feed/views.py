import json

from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings

from accounts.models import User
from .models import Place, Review
from .forms import ReviewForm


class Index(generic.ListView):
    template_name = 'feed/index.html'
    context_object_name = 'celebrity_list'

    def get_queryset(self):
        return User.objects.all()


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


def redirectToPlace(request):
    data=json.loads(request.body)
    id = data['id']
    try:
        place = Place.objects.get(id=id) 
    except:
        place = Place(
            id=id,
            place_name=data['place_name'],
            place_url=data['place_url'],
            phone=data['phone'],
            category_name=data['category_name'],
            category_group_name=data['category_group_name'],
            category_group_code=data['category_group_code'],
            address_name=data['address_name'],
            road_address_name=data['road_address_name'],
            x=data['x'],
            y=data['y'],
        )
        place.save()
    finally:
        return redirect('feed:place_profile', id)


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


class WriteReview(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'feed/review_form.html'

    model = Review
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = get_object_or_404(Place, id=self.kwargs.get("id"))
        return context

    def form_valid(self, form):
        form.instance.place = get_object_or_404(Place, id=self.kwargs.get("id"))
        form.instance.user = self.request.user
        return super().form_valid(form)


class Explore(LoginRequiredMixin, generic.ListView):
    def get_context_data(self, **kwargs):
        user = self.request.user
        following_list = user.following.all()

        context = super().get_context_data(**kwargs)
        context['following_list'] = following_list
        return context

    def get_queryset(self):
        return Review.objects.all()


class ExploreMap(Explore):
    template_name = 'feed/map.html'


class ExploreTimeline(Explore):
    template_name = 'feed/timeline.html'


@login_required
def follow(request, username):
    request.user.follow(username)
    return redirect('feed:user_profile', username)

@login_required
def unfollow(request, username):
    request.user.unfollow(username)
    return redirect('feed:user_profile', username)
