from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='blog-home'),
    path('about/', views.about_views, name='blog-about'),
]