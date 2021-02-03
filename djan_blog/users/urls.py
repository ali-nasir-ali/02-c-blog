from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_views, name="register_users" ),
    path('', views.about_views, name="blog_about" ),
]
