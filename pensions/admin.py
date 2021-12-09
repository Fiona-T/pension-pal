"""Register the models for the 'pensions' app for admin panel"""
from django.contrib import admin
from .models import Provider

admin.site.register(Provider)
