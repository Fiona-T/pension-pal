"""Unit tests for Views for 'jobs' app"""
from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """To test the views for 'jobs' app"""
    def test_get_my_jobs_page(self):
        """
        get url for my-jobs page, check the response is 200 (i.e. successful)
        check the correct template is used
        """
        response = self.client.get('/jobs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-jobs.html')
