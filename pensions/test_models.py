"""Unit tests for Models for 'jobs' app"""
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from jobs.models import Job
from .models import Provider, Pension


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


class TestPensionModel(TestCase):
    """Tests for Pensions model in pensions app"""
    @classmethod
    def setUpTestData(cls):
        """
        Create user, job and provider for tests
        These are foreign keys in Pension model so are needed to create records
        """
        test_user = User.objects.create_user(
            username='Tester',
            password='topsecret1234',
        )
        test_user.save()

        Job.objects.create(
            added_by=User.objects.get(username='Tester'),
            employer_name='Test Company',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
            )

        Provider.objects.create(
            provider_name='A Pension Provider',
            website='wwww.awebsite.ie',
            status=1,
        )

    def test_pension_type_defaults_to_occupational(self):
        """
        Create a record with Pension model without setting pension type field
        check this field was set to Occupational Pension Scheme (0)
        """
        pension = Pension.objects.create(
            added_by=User.objects.get(username='Tester'),
            employment=Job.objects.get(id=1),
            scheme_name='Test pension scheme',
            policy_number='12345',
            date_joined_scheme='2020-01-01',
            salary=10000,
            pension_provider=Provider.objects.get(id=1),
            value=1000,
            )
        self.assertEqual(pension.pension_type, 0)

    def test_pension_string_method_returns_scheme_name_and_user(self):
        """
        Check that string method called on a record returns: the scheme
        name + 'for' + user name
        """
        pension = Pension.objects.create(
            added_by=User.objects.get(username='Tester'),
            employment=Job.objects.get(id=1),
            scheme_name='Test pension scheme',
            policy_number='12345',
            pension_type=1,
            date_joined_scheme='2020-01-01',
            salary=10000,
            pao=True,
            director=True,
            pension_provider=Provider.objects.get(id=1),
            value=1000,
            )
        self.assertEqual(str(pension), 'Test pension scheme for Tester')
