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


class TestAddPensionView(TestCase):
    """ To test the AddPension view """
    @classmethod
    def setUpTestData(cls):
        """
        Create a test user.
        Create job and provider, needed as foreign keys in Pension
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

    def test_redirects_if_not_logged_in(self):
        """ Test that user is redirected to correct page if not logged in """
        response = self.client.get('/pensions/add/')
        self.assertRedirects(response, '/accounts/login/?next=/pensions/add/')

    def test_correct_url_and_template_for_logged_in_user(self):
        """
        login the test user, get the url for add-pension page
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/add/')
        self.assertEqual(str(response.context['user']), 'Tester')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-pension.html')

    def test_can_add_pension(self):
        """
        login the test user, get pensions url, check length of pension_list is
        0 initially. Then do POST request on add pension url, with test pension
        data, including ids from foreign key fields
        Check redirects to the correct success url after adding
        Check that length of pension_list is now 1
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/')
        self.assertEqual(len(response.context['pension_list']), 0)
        response = self.client.post('/pensions/add/', {
            'added_by': 'Tester',
            'employment': str(1),
            'scheme_name': "Test Company Pension Scheme",
            'policy_number': '876934B',
            'pension_type': 1,
            'date_joined_scheme': '2020-01-01',
            'salary': 50000,
            'pao': False,
            'director': True,
            'pension_provider': str(1),
            'value': 36789,
        })
        self.assertRedirects(response, '/pensions/success/')
        response = self.client.get('/pensions/')
        self.assertEqual(len(response.context['pension_list']), 1)


class TestEditPensionView(TestCase):
    """Tests for the EditPension view"""
    @classmethod
    def setUpTestData(cls):
        """
        Create two test users.
        Create provider and 2 job records, needed as foreign keys in Pension
        Create a pension record. All records created by test_user1.
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

        Job.objects.create(
            added_by=User.objects.get(username='Tester'),
            employer_name='Second Test Company',
            start_date='2004-04-15',
            finish_date='2020-12-01',
            full_or_part_time=0,
            )

        Provider.objects.create(
            provider_name='A Pension Provider',
            website='wwww.awebsite.ie',
            status=1,
            )

        Pension.objects.create(
            added_by=test_user1,
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
        """User is redirected to correct page if not logged in"""
        response = self.client.get('/pensions/edit/1')
        self.assertRedirects(
            response, '/accounts/login/?next=/pensions/edit/1'
            )

    def test_correct_url_and_template_for_logged_in_user_own_pensions(self):
        """
        Login the test user, get the url for edit-pension page, using id of 1
        (this will be the id of the pension added in set up)
        check the user is logged in, that the response is 200 (i.e. successful)
        and check the correct template is used
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/edit/1')
        self.assertEqual(str(response.context['user']), 'Tester')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-pension.html')

    def test_can_edit_own_pension_detail(self):
        """
        Login test user, go to edit url, post to edit url with update to some
        fields. Check redirects to my-pensions page after form submitted.
        Get the pension record, check the fields have the updated details.
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/edit/1')
        response = self.client.post('/pensions/edit/1', {
            'added_by': 'Tester',
            'employment': str(2),
            'scheme_name': "New Pension Scheme Name",
            'policy_number': '12345',
            'pension_type': 1,
            'date_joined_scheme': '2020-01-01',
            'salary': 50000,
            'pao': False,
            'director': False,
            'pension_provider': str(1),
            'value': 36789,
            })
        self.assertRedirects(response, '/pensions/')
        updated_pension = Pension.objects.get(id=1)
        self.assertEqual(
            updated_pension.scheme_name, 'New Pension Scheme Name'
            )
        self.assertEqual(
            str(updated_pension.employment), 'Second Test Company'
            )
        self.assertEqual(updated_pension.salary, 50000)
        self.assertEqual(updated_pension.pao, False)
        self.assertEqual(updated_pension.director, False)
        self.assertEqual(updated_pension.value, 36789)

    def test_404_returned_logged_in_but_invalid_pension_id(self):
        """
        Logged in user gets 404 response trying to access edit page using
        an invalid pension id, i.e one which does not exist
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/edit/5')
        self.assertEqual(response.status_code, 404)

    def test_cannot_access_edit_page_for_other_user_pension(self):
        """
        Logged in user who did not create the pension gets 404 response when
        trying to access the edit page with pension id not created by them
        """
        self.client.login(username='jane', password='secret1234567')
        response = self.client.get('/pensions/')
        self.assertEqual(str(response.context['user']), 'jane')
        response = self.client.get('/pensions/edit/1')
        self.assertEqual(response.status_code, 404)


class TestDeletePensionView(TestCase):
    """Tests for the Delete Pension View"""
    @classmethod
    def setUp(cls):
        """
        Create a test user.
        Create provider and job records, needed as foreign keys in Pension
        Create a pension record.
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

        Pension.objects.create(
            added_by=test_user,
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

    def test_can_delete_pension(self):
        """
        Login the test user, go to pensions page, pension_list length should
        be 1. Post the delete request with the pension id created above.
        Check page redirects back to pensions page, and that length of pension
        list is now 0 since the record created in set up was deleted.
        """
        self.client.login(username='Tester', password='topsecret1234')
        response = self.client.get('/pensions/')
        self.assertEqual(len(response.context['pension_list']), 1)
        response = self.client.post('/pensions/delete/1')
        self.assertRedirects(response, '/pensions/')
        response = self.client.get('/pensions/')
        self.assertEqual(len(response.context['pension_list']), 0)
