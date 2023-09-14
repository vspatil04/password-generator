
from django.urls import include, path
from .  import views


urlpatterns = [
     path('password_generator/', views.home, name='password_generator'),

    
]
"""
from django.urls import path
from . import views

app_name = 'password_generator'  # Optional, but useful for namespacing URLs

urlpatterns = [
    path('generate-password/', views.password_generator, name='generate_password'),
]"""
