"""Register the models for the 'jobs' app for admin panel"""
from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Job model - admin set up:
    Show all fields in list display, allow filtering by user who added record,
    Allow search by employer name. Employer name is a link to view the record.
    Id field shown as readonly field for information purposes.
    """
    readonly_fields = ('id',)
    list_display = (
        'added_by',
        'employer_name',
        'start_date',
        'finish_date',
        'full_or_part_time'
        )
    list_filter = ('added_by',)
    list_display_links = ('employer_name',)
    search_fields = ['employer_name']
