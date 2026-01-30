from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create_view, name='create'),
    path('create_stud/', views.create_student, name='create_student'),
    path('update/<int:id>/', views.update_view, name="update"),
    path('update/save/<int:id>/', views.update_student, name="update_save"),
    path('delete/<int:id>/', views.delete_student, name="delete"),
]