"""Unit tests for Views for 'jobs' app"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Job


class TestMyJobsListView(TestCase):
    """ To test the MyJobs listview """
    @classmethod
    def setUpTestData(cls):
        """
        Create two test users. Create test job records, half added_by user1 and
        half added by user2. So that listview filtered by user can be tested
        10 jobs per user to check the pagination
        When creating job records, add job index number to company name, to
        avoid failing the unique constraint test on employer_name per user
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
                employer_name=f'Test Company {job}',
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
        """ Create a test user and one Job record """
        test_user = User.objects.create_user(
            username='fred',
            password='secret1234',
        )
        test_user.save()
        Job.objects.create(
            added_by=test_user,
            employer_name='Same Name',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
        )

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
        one initially (existing job created in setup). Then do POST request on
        add job url, with test job. Check redirects to the correct success url
        after adding. Check that length of job_list is now 2
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 1)
        response = self.client.post('/jobs/add/', {
            'added_by': 'user',
            'employer_name': 'Test Company',
            'start_date': '2020-01-01',
            'finish_date': '2020-12-01',
            'full_or_part_time': 1,
        })
        self.assertRedirects(response, '/jobs/success/')
        response = self.client.get('/jobs/')
        self.assertEqual(len(response.context['job_list']), 2)

    def test_error_raised_on_employer_name_unique_constraint(self):
        """
        login the test user, Do POST request on add job url, with same
        employer_name as existing job record for that user.
        Check it does not redirect (i.e. status code is 200, not 302)
        Check the form error text is present (non_field_error)
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.post('/jobs/add/', {
            'added_by': 'fred',
            'employer_name': 'Same Name',
            'start_date': '2021-01-01',
            'finish_date': '2022-12-01',
            'full_or_part_time': 1,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            'form',
            None,
            'You already have a Job with this Employer name. Choose a '
            'different name for this new Job record.'
            )


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
        """
        Create a test user and two job records
        Create a second test user with no job records
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

        Job.objects.create(
            added_by=test_user1,
            employer_name='Test Company',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
        )
        Job.objects.create(
            added_by=test_user1,
            employer_name='Same Name',
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

    def test_message_is_displayed_for_successful_edit(self):
        """
        Login testuser1, post edit job request.
        Check page redirects back to jobs page, get the messages,
        Check length is 1 and that msg tag and content are correct.
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.post('/jobs/edit/1', {
            'added_by': 'user',
            'employer_name': 'Test Company New Name',
            'start_date': '2020-01-01',
            'finish_date': '2020-12-01',
            'full_or_part_time': 1,
            })
        self.assertRedirects(response, '/jobs/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'alert-success')
        self.assertEqual(
            messages[0].message,
            'Edited details for Job: "Test Company New Name" successfully'
            ' saved.'
            )

    def test_unique_constraint_for_employer_name_per_user_on_edit(self):
        """
        login the test user, Do POST request on edit job url for job id 1,
        amending employer_name to same as job id 2 for that user.
        Check it does not redirect (i.e. status code is 200, not 302)
        Check the form error text is present (non_field_error)
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.post('/jobs/edit/1', {
            'added_by': 'fred',
            'employer_name': 'Same Name',
            'start_date': '2020-01-01',
            'finish_date': '2020-12-01',
            'full_or_part_time': 0,
            })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            'form',
            None,
            'You already have a Job with this Employer name. Choose a '
            'different name for this new Job record.'
            )

    def test_404_returned_logged_in_but_invalid_job_id(self):
        """
        Logged in user gets 404 response trying to access edit page using
        an invalid job id, i.e one which does not exist
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/edit/5')
        self.assertEqual(response.status_code, 404)

    def test_cannot_access_edit_page_for_other_user_job(self):
        """
        Logged in user who did not create the job gets 404 response when
        trying to access the edit page with job id not created by them
        """
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/jobs/')
        self.assertEqual(str(response.context['user']), 'jane')
        response = self.client.get('/jobs/edit/1')
        self.assertEqual(response.status_code, 404)


class TestDeleteJobView(TestCase):
    """Tests for the Delete Job View"""
    @classmethod
    def setUp(cls):
        """
        Create a test user and a job record
        Create a second test user with no job record
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

        Job.objects.create(
            added_by=test_user1,
            employer_name='Test Company to delete',
            start_date='2020-01-01',
            finish_date='2020-12-01',
            full_or_part_time=1,
        )

    def test_redirects_if_not_logged_in(self):
        """
        User not logged in and trying to access delete url is redirected to
        sign in page
        """
        response = self.client.get('/jobs/delete/1')
        self.assertRedirects(response, '/accounts/login/?next=/jobs/delete/1')

    def test_404_raised_for_get_request_on_delete_url(self):
        """
        Login test user1, try to access delete url via get request
        Should get 404 error since the delete view is post only
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.get('/jobs/delete/1')
        self.assertEqual(response.status_code, 404)

    def test_cannot_delete_job_record_of_different_user(self):
        """
        Login test user2 (no job records), try to access the delete url for job
        id of test user1, via post request. Should get error 404 since job id
        does not belong to that user
        """
        self.client.login(username='jane', password='secret1234567')
        response = self.client.post('/jobs/delete/1')
        self.assertEqual(response.status_code, 404)

    def test_can_delete_own_job(self):
        """
        Login testuser1, go to jobs page, job_list length should be 1
        Post the delete request with the job id created above
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

    def test_message_is_displayed_for_successful_deletion(self):
        """
        Login testuser1, post the delete job request with job id created
        above. Check page redirects back to jobs page, get the messages,
        check length is 1 and that msg tag and content are correct.
        """
        self.client.login(username='fred', password='secret1234')
        response = self.client.post('/jobs/delete/1')
        self.assertRedirects(response, '/jobs/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'alert-success')
        self.assertEqual(
            messages[0].message,
            'Job: "Test Company to delete" successfully deleted.'
            )
