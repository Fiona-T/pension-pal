"""Models for the 'pensions' app (create, view, edit, delete pensions)"""
from django.db import models

STATUS = ((0, 'Active'), (1, 'Not active'))


class Provider(models.Model):
    """Model for pension provider details, records added in admin panel"""
    provider_name = models.CharField(max_length=50, unique=True)
    website = models.URLField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """order the records by name of provider"""
        ordering = ['provider_name']

    def __str__(self):
        return self.provider_name
