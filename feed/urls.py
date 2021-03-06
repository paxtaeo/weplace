from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('users/<str:username>/', views.UserProfile.as_view(), name='user_profile'),

    path('places/create/', views.redirectToPlace, name='redirct-to-place'),
    path('places/<str:id>/', views.PlaceProfile.as_view(), name='place_profile'),
    path('places/<str:id>/write', views.WriteReview.as_view(), name='write-review'),

    path('explore/map/', views.ExploreMap.as_view(), name='explore-map'),
    path('explore/timeline/', views.ExploreTimeline.as_view(), name='explore-timeline'),

    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]
