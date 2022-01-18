"""Register the models for the 'pensions' app for admin panel"""
from django.contrib import admin
from .models import Provider, Pension


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    """
    Provider model - admin set up:
    Show all fields in list display, allow filtering by status,
    Allow search by provider name or website.
    Allow editing of website and status via list view.
    """
    list_display = ('provider_name', 'website', 'status')
    list_filter = ('status', )
    list_editable = ('website', 'status')
    search_fields = ['provider_name', 'website']


admin.site.register(Pension)
