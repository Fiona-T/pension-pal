"""Unit tests for Views for 'jobs' app"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job


class TestMyJobsListView(TestCase):
    """ To test the MyJobs listview """
    def setUp(self):
        """
        Create two test users. Create test job records, half added_by user1 and
        half added by user2. So that listview filtered by user can be tested
        """
        test_user1 = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user2 = User.objects.create_user(
            username='jane',
            password='secret1234567',
        )
        test_user1.save()
        test_user2.save()

        number_of_jobs = 10
        for job in range(number_of_jobs):
            added_by_user = test_user1 if job % 2 else test_user2
            Job.objects.create(
                added_by=added_by_user,
                employer_name='Test Company',
                start_date='2020-01-01',
                finish_date='2020-12-01',
                full_or_part_time=1,
            )

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/jobs/')
        self.assertRedirects(response, '/accounts/login/?next=/jobs/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for my-jobs page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/')
        self.assertEqual(str(response.context['user']), 'fred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-jobs.html')

    def test_jobs_displayed_belong_to_loggedin_user(self):
        """
        login the test user, get the url for my-jobs page
        check the user is logged in, check jobs_list is returned
        and the jobs displayed are those with added_by equal to user
        """
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/jobs/')
        self.assertEqual(str(response.context['user']), 'jane')
        self.assertTrue('job_list' in response.context)
        for job in response.context['job_list']:
            self.assertEqual(response.context['user'], job.added_by)


class TestAddJobView(TestCase):
    """ To test the AddJob view """
    def setUp(self):
        """ Create a test user """
        test_user = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user.save()

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/jobs/add/')
        self.assertRedirects(response, '/accounts/login/?next=/jobs/add/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for add-job page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/add/')
        self.assertEqual(str(response.context['user']), 'fred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-job.html')
