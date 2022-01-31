from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', views.UserCreate.as_view(), name='register'),
    path('register/done/', views.UserCreateDone.as_view(), name='register-done'),
]
