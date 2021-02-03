from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_views, name="register_users" ),
    path('profile/', views.profile_views, name="profile_user" ),
]
