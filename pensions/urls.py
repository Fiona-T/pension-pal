"""URL paths for the 'pensions' app (add, view, edit, delete pension)"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyPensions.as_view(), name='my_pensions'),
]
