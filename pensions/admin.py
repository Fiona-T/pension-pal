"""Register the models for the 'pensions' app for admin panel"""
from django.contrib import admin
from .models import Provider, Pension

admin.site.register(Provider)

admin.site.register(Pension)
