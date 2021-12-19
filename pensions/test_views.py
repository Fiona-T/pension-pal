"""Unit tests for Views for 'pensions' app"""
from django.test import TestCase
from django.contrib.auth.models import User
from jobs.models import Job
from .models import Pension, Provider


class TestMyPensionsListView(TestCase):
    """ To test the MyPensions listview """
    @classmethod
    def setUpTestData(cls):
        """
        Create two test users. Create job and provider, needed as foreign keys
        Create test pension records, half added_by user1, half added by user2.
        So that listview filtered by user can be tested
        10 pensions per user to check the pagination
        """
        test_user1 = User.objects.create_user(
            username='Tester',
            password='topsecret1234',
        )
        test_user2 = User.objects.create_user(
            username='jane',
            password='secret1234567',
        )
        test_user1.save()
        test_user2.save()

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

        number_of_pensions = 20
        for pension in range(number_of_pensions):
            added_by_user = test_user1 if pension % 2 else test_user2
            Pension.objects.create(
                added_by=added_by_user,
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

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/pensions/')
        self.assertRedirects(response, '/accounts/login/?next=/pensions/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for my-pensions page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/')
        self.assertEqual(str(response.context['user']), 'Tester')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-pensions.html')

    def test_pensions_displayed_belong_to_loggedin_user(self):
        """
        login the test user, get the url for my-pensions page
        check the user is logged in, check pensions_list is returned
        and the pensions displayed are those with added_by equal to user
        """
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/pensions/')
        self.assertEqual(str(response.context['user']), 'jane')
        self.assertTrue('pension_list' in response.context)
        for pension in response.context['pension_list']:
            self.assertEqual(response.context['user'], pension.added_by)

    def test_paginated_by_6(self):
        """Check results are paginated, with 6 per page"""
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/pensions/')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['pension_list']), 6)


class TestAddPensionSuccessView(TestCase):
    """ To test the AddPensionSuccess view """
    @classmethod
    def setUpTestData(cls):
        """ Create a test user """
        test_user = User.objects.create_user(
            username='Tester',
            password='topsecret1234',
        )
        test_user.save()

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/pensions/success/')
        self.assertRedirects(response, '/accounts/login/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for add-pension-success page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/success/')
        self.assertEqual(str(response.context['user']), 'Tester')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-pension-success.html')
