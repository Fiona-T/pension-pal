"""URL paths for the 'jobs' app (add, view, edit, delete jobs)"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyJobs.as_view(), name='my_jobs'),
]
