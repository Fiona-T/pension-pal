"""Unit tests for Models for 'jobs' app"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job


class TestModels(TestCase):
    """To test the model for 'jobs' app"""
    @classmethod
    def setUpTestData(cls):
        """
        Create a user for tests, user needed to create records from Job model
        """
        test_user = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user.save()

    def test_full_or_part_time_defaults_to_full(self):
        """
        Create a record from Job model without setting the
        full_or_part_time field, check this field was set to full
        """
        job = Job.objects.create(
            added_by=User.objects.get(username='fred'),
            employer_name='Test employer',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            )
        self.assertEqual(job.full_or_part_time, 0)

    def test_job_string_method_returns_employer_name(self):
        """
        Check that employer name created in test record is returned
        by the string method called on that record
        """
        job = Job.objects.create(
            added_by=User.objects.get(username='fred'),
            employer_name='Test Company',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
            )
        self.assertEqual(str(job), 'Test Company')
