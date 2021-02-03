from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name="blog_home" ),
    path('', views.about_views, name="blog_about" ),
]
