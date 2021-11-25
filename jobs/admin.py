"""Register the models for the 'jobs' app for admin panel"""
from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)
