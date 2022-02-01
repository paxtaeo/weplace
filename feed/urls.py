from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('users/<str:username>/', views.UserProfile.as_view(), name='user_profile'),
    path('places/<str:id>/', views.PlaceProfile.as_view(), name='place_profile'),
    path('explore/', views.Explore.as_view(), name='explore'),

    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),

    path('reviews/create', views.ReviewCreate.as_view(), name='review-create'),
]
