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


@admin.register(Pension)
class PensionAdmin(admin.ModelAdmin):
    """
    Pension model - admin set up:
    Show all user, scheme name, employment and value in list display,
    Allow filtering by user who added the record, or by pension provider.
    Allow search by employment (foreign key) or by scheme_name.
    Scehme name is a link to view the record.
    Id field shown as readonly field for information purposes.
    """
    readonly_fields = ('id',)
    list_display = ('added_by', 'scheme_name', 'employment', 'value')
    list_filter = ('added_by', 'pension_provider')
    list_display_links = ('scheme_name',)
    search_fields = ['employment__employer_name', 'scheme_name']
