from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public pages
    path('', views.index, name='index'),  # Homepage
    path('about/', views.about, name='about'),  # About page

    # Protected pages (login required)
    path('candles/', views.candles, name='candles'),  # List of candles (requires login)
    path('room_sprays/', views.room_sprays, name='room_sprays'),  # List of room sprays (requires login)

    # User authentication URLs
    path('register/', views.register, name='register'),  # User registration page
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='products/login.html'), 
        name='login'
    ),  # User login page using Django's built-in LoginView with custom template
    path(
        'logout/', 
        auth_views.LogoutView.as_view(next_page='index'), 
        name='logout'
    ),  # User logout URL; redirects to homepage after logout
]
