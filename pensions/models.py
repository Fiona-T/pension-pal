"""Models for the 'pensions' app (create, view, edit, delete pensions)"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from jobs.models import Job

STATUS = ((0, 'Active'), (1, 'Not active'))
PENSION_TYPE = (
    (0, 'Occupational Pension Scheme'),
    (1, 'PRSA'),
    (2, 'RAC / Personal Pension'),
    (3, 'Retirement Bond'),
    )


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


class Pension(models.Model):
    """Model for Pension records added by user via form on frontend"""
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pensions')
    employment = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='linked_pensions')
    scheme_name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=15)
    member_number = models.CharField(max_length=15, blank=True)
    pension_type = models.IntegerField(choices=PENSION_TYPE, default=0)
    date_joined_scheme = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    pao = models.BooleanField(default=False)
    director = models.BooleanField(default=False)
    pension_provider = models.ForeignKey(
        Provider, on_delete=models.PROTECT, related_name='recorded_pensions')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    file = CloudinaryField('image', blank=True,)
    notes = models.TextField(blank=True)

    class Meta:
        """order by date joined the scheme"""
        ordering = ['-date_joined_scheme']

    def __str__(self):
        return f'{self.scheme_name} for {self.added_by}'
