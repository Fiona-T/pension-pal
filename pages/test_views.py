"""Unit tests for Views for 'pages' app (static pages)"""
from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """To test the views for 'pages' app which handles static pages"""
    def test_home_page_view(self):
        """
        get the url for home page, check the response is 200 (i.e. successful)
        check the correct template is used
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
