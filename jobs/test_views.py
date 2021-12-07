"""Unit tests for Views for 'jobs' app"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job


class TestMyJobsListView(TestCase):
    """ To test the MyJobs listview """
    @classmethod
    def setUpTestData(cls):
        """
        Create two test users. Create test job records, half added_by user1 and
        half added by user2. So that listview filtered by user can be tested
        10 jobs per user to check the pagination
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

        number_of_jobs = 20
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

    def test_paginated_by_6(self):
        """Check results are paginated, with 6 per page"""
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/jobs/')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['job_list']), 6)


class TestAddJobView(TestCase):
    """ To test the AddJob view """
    @classmethod
    def setUpTestData(cls):
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

    def test_can_add_job(self):
        """
        login the test user, get jobs url and check length of job_list is
        zero initially. Then do POST request on add job url, with test job
        check redirects to the correct success url after adding
        check that length of job_list is now 1
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 0)
        response = self.client.post('/jobs/add/', {
            'added_by': 'user',
            'employer_name': 'Test Company',
            'start_date': '2020-01-01',
            'finish_date': '2020-12-01',
            'full_or_part_time': 1,
        })
        self.assertRedirects(response, '/jobs/success/')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 1)


class TestAddJobSuccessView(TestCase):
    """ To test the AddJobSuccess view """
    @classmethod
    def setUpTestData(cls):
        """ Create a test user """
        test_user = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user.save()

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/jobs/success/')
        self.assertRedirects(response, '/accounts/login/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for add-job-success page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/success/')
        self.assertEqual(str(response.context['user']), 'fred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-job-success.html')


class TestEditJobView(TestCase):
    """Tests for the EditJob view"""
    @classmethod
    def setUp(cls):
        """Create a test user and a job record"""
        test_user1 = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user1.save()

        Job.objects.create(
            added_by=test_user1,
            employer_name='Test Company',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
        )

    def test_redirects_if_not_logged_in(self):
        """User is redirected to correct page if not logged in"""
        response = self.client.get('/jobs/edit/1')
        self.assertRedirects(response, '/accounts/login/?next=/jobs/edit/1')

    def test_correct_url_and_template_for_logged_in_user_own_job(self):
        """
        Login the test user, get the url for edit-job page, using id of 1
        (this will be the id of the job added in set up)
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/edit/1')
        self.assertEqual(str(response.context['user']), 'fred')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-job.html')

    def test_can_edit_own_job_detail(self):
        """
        Login test user, go to edit url, post to edit url with updates to name
        and full/parttime fields. Check redirects to my-jobs page after form.
        Get the job record, check that the two fields have the updated details.
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/edit/1')
        response = self.client.post('/jobs/edit/1', {
            'added_by': 'user',
            'employer_name': 'Test Company Changed Name',
            'start_date': '2020-01-01',
            'finish_date': '2020-12-01',
            'full_or_part_time': 0,
            })
        self.assertRedirects(response, '/jobs/')
        updated_job = Job.objects.get(id=1)
        self.assertEqual(
            updated_job.employer_name, 'Test Company Changed Name'
            )
        self.assertEqual(updated_job.full_or_part_time, 0)

    def test_404_returned_logged_in_but_invalid_job_id(self):
        """
        Logged in user gets 404 response trying to access edit page using
        an invalid job id, i.e one which does not exist
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/edit/5')
        self.assertEqual(response.status_code, 404)


class TestDeleteJobView(TestCase):
    """Tests for the Delete Job View"""
    @classmethod
    def setUp(cls):
        """Create a test user and a job record"""
        test_user1 = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user1.save()

        Job.objects.create(
            added_by=test_user1,
            employer_name='Test Company to delete',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
        )

    def test_can_delete_job(self):
        """
        Login the test user, go to jobs page, job_list length should be 1
        Post the delete request with the job ide created above
        Check page redirects back to jobs page, and that length of jobs list
        is now 0 since the record created in set up was deleted.
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 1)
        response = self.client.post('/jobs/delete/1')
        self.assertRedirects(response, '/jobs/')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 0)
