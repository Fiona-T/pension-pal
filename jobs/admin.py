"""Register the models for the 'jobs' app for admin panel"""
from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    """Admin panel set up for Job model - show the id field"""
    readonly_fields = ('id',)


admin.site.register(Job, JobAdmin)
