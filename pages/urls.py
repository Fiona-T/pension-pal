"""URL paths for the 'pages' app (static pages)"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
