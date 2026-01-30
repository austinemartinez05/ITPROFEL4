from django.urls import path
from . import views

urlpatterns=[
    path('users/', views.users, name='users'),
    path('profile/',views.profile, name='users'),
    path('registration/',views.registration, name='users')
]