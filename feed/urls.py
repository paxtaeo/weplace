from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('users/<str:username>/', views.Profile.as_view(), name='profile'),
]
