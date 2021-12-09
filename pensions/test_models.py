"""Unit tests for Models for 'jobs' app"""
from django.test import TestCase
from django.db import IntegrityError
from .models import Provider


class TestProviderModel(TestCase):
    """tests for Provider model in pensions app"""
    def test_status_defaults_to_active(self):
        """
        Create a record without setting status
        Check status is 0, i.e. active
        """
        provider = Provider.objects.create(
            provider_name='Test Provider',
            website='www.website.com',
        )
        self.assertEqual(provider.status, 0)

    def test_string_method_returns_provider_name(self):
        """
        Create a record, check that the string method called on this
        record returns the provider_name
        """
        provider = Provider.objects.create(
            provider_name='A Pension Provider',
            website='wwww.awebsite.ie',
            status=1,
        )
        self.assertEqual(str(provider), 'A Pension Provider')

    def test_provider_name_is_unique_in_table(self):
        """
        Create a record, then check that creating another record with the
        same provider_name raises an error
        """
        Provider.objects.create(
            provider_name='Test Provider',
            website='www.website.com',
        )

        with self.assertRaises(IntegrityError):
            Provider.objects.create(
                provider_name='Test Provider',
                website='www.websitename.com',
                status=1,
            )
