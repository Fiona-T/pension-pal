"""Unit tests for Forms for 'pensions' app"""
import os
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from jobs.models import Job
from .forms import PensionForm
from .models import Provider

# test files for file field testing located here
TEST_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data'
    )


class TestPensionForm(TestCase):
    """Test the Pension form - add/edit pension """
    @classmethod
    def setUpTestData(cls):
        """
        Create test user, test job and two test providers,
        needed as foreign keys to submit pension form with data.
        Test providers - one active and one not active so can test filter
        """
        User.objects.create_user(
            username='Tester',
            password='topsecret1234',
        )
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
        Provider.objects.create(
            provider_name='An Active Pension Provider',
            website='wwww.awebsite.ie',
            status=0,
        )

    def test_file_field_help_text(self):
        """Test that the Upload file field has the associated help text """
        form = PensionForm()
        self.assertEqual(
            form.fields['file'].help_text,
            'Upload your most recent annual benefit statement, '
            'or any other relevant file.<br><strong>Note: only .jpg or .png '
            'files allowed</strong>'
            )

    def test_employment_field_help_text(self):
        """Test that the Employment field has correct associated help text """
        form = PensionForm()
        self.assertEqual(
            form.fields['employment'].help_text,
            'If the Job is not in the list, go to My Jobs to add the Job'
            ' record first.'
            )

    def test_widget_exists_on_date_joined_scheme_field_(self):
        """Test that date_joined_scheme field has DateInput widget attached """
        form = PensionForm()
        field = form.fields['date_joined_scheme']
        self.assertEqual(
            field.widget.__class__.__name__, 'DateInput'
            )

    def test_employment_field_selected_choice(self):
        """Test Employment field has 'selected' option at top of dropdown """
        form = PensionForm()
        self.assertEqual(
            form.fields['employment'].empty_label,
            'Choose Job the pension relates to'
            )

    def test_provider_field_selected_choice(self):
        """Test Provider field has 'selected' option at top of dropdown """
        form = PensionForm()
        self.assertEqual(
            form.fields['pension_provider'].empty_label,
            'Choose pension provider'
            )

    def test_explicitly_set_field_labels_exist(self):
        """
        Check labels are present for the fields where a label was explicitly
        set in the form Meta class
        """
        form = PensionForm()
        self.assertTrue(
            form.fields['salary'].label is None or
            form.fields['salary'].label == 'Salary at date of leaving service'
            )
        self.assertTrue(
            form.fields['pao'].label is None or
            form.fields['pao'].label == 'Is there a Pension Adjustment Order '
            '(PAO) on the pension?'
            )
        self.assertTrue(
            form.fields['director'].label is None or
            form.fields['director'].label == 'Were you a 20% director in this '
            'employment?'
            )
        self.assertTrue(
            form.fields['value'].label is None or
            form.fields['value'].label == 'Current value of pension scheme'
            )
        self.assertTrue(
            form.fields['file'].label is None or
            form.fields['file'].label == 'Upload recent statement'
            )
        self.assertTrue(
            form.fields['notes'].label is None or
            form.fields['notes'].label == 'Additional notes on this pension'
            )

    def test_required_fields_are_required(self):
        """
        Create a form without any details filled in, check that it is not valid
        Check that each required field name key is in the keys of the form
        errors dict. Check that error returned for each empty field is correct
        """
        form = PensionForm({
            'added_by': '',
            'employment': '',
            'scheme_name': '',
            'policy_number': '',
            'member_number': '',
            'pension_type': '',
            'date_joined_scheme': '',
            'salary': '',
            'pao': '',
            'director': '',
            'pension_provider': '',
            'value': '',
            'file': '',
            'notes': '',
        })

        self.assertFalse(form.is_valid())
        # required fields
        self.assertIn('employment', form.errors.keys())
        self.assertIn('scheme_name', form.errors.keys())
        self.assertIn('policy_number', form.errors.keys())
        self.assertIn('pension_type', form.errors.keys())
        self.assertIn('date_joined_scheme', form.errors.keys())
        self.assertIn('salary', form.errors.keys())
        self.assertIn('pension_provider', form.errors.keys())
        self.assertIn('value', form.errors.keys())

        # not required fields
        self.assertNotIn('member_number', form.errors.keys())
        self.assertNotIn('pao', form.errors.keys())
        self.assertNotIn('director', form.errors.keys())
        self.assertNotIn('file', form.errors.keys())
        self.assertNotIn('notes', form.errors.keys())

        # error message exists for required fields
        self.assertEqual(
            form.errors['employment'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['scheme_name'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['policy_number'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['pension_type'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['date_joined_scheme'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['salary'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['pension_provider'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['value'][0], 'This field is required.'
            )

    def test_pension_type_defaults_to_occupational(self):
        """Check initial value on full_or_part_time is fulltime (0) """
        form = PensionForm()
        self.assertEqual(form['pension_type'].initial, 0)

    def test_pension_provider_field_choices_only_include_active(self):
        """
        Create form, get the choices from the pension_provider field.
        Choices should contain the 'Choose pension provider' selected option
        and the one active pension provider (and not the inactive one), so the
        length should be 2.
        """
        form = PensionForm()
        choices = list(form.fields['pension_provider'].choices)
        self.assertEqual(len(choices), 2)
        self.assertEqual(str(choices[0][1]), 'Choose pension provider')
        self.assertEqual(str(choices[1][1]), 'An Active Pension Provider')

    def test_cannot_add_form_with_not_active_pension_provider(self):
        """
        Create form with pension provider that is not active. Confirm there are
        form errors and form is not valid, and error msg is as expected.
        """
        form = PensionForm({
            'added_by': User.objects.get(username='Tester'),
            'employment': Job.objects.get(employer_name='Test Company'),
            'scheme_name': 'My Pension Scheme',
            'policy_number': '124',
            'member_number': '123',
            'pension_type': 1,
            'date_joined_scheme': '2020-01-01',
            'salary': '40000',
            'pao': 'false',
            'director': 'false',
            'pension_provider': Provider.objects.get(
                provider_name='A Pension Provider'
                ),
            'value': '3000',
            'notes': '',
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('pension_provider', form.errors.keys())
        self.assertEqual(
            form.errors['pension_provider'][0],
            'Select a valid choice. That choice is not one of the '
            'available choices.'
            )

    def test_error_raised_on_file_field_for_docx_extension(self):
        """
        Create form using a word document .docx file. Confirm there are
        form errors. Check file is in the form.errors keys dictionary
        Check the content of the error message is as expected.
        """
        data = {
            'added_by': User.objects.get(username='Tester'),
            'employment': Job.objects.get(employer_name='Test Company'),
            'scheme_name': 'My Pension Scheme',
            'policy_number': '124',
            'member_number': '123',
            'pension_type': 1,
            'date_joined_scheme': '2020-01-01',
            'salary': '40000',
            'pao': 'false',
            'director': 'false',
            'pension_provider': Provider.objects.get(
                provider_name='A Pension Provider'
                ),
            'value': '3000',
            'notes': '',
        }

        test_file = os.path.join(TEST_DIR, 'test-upload-word-file.docx')
        with open(test_file, 'rb') as file:
            form = PensionForm(data=data, files={
                'file': SimpleUploadedFile('file', file.read())
                })
        self.assertTrue(form.errors)
        self.assertIn('file', form.errors.keys())
        self.assertEqual(
            form.errors['file'][0],
            'File type must be .png or .jpg. Choose a different file '
            'of the correct type'
            )

    def test_error_raised_on_file_field_for_pdf_extension(self):
        """
        Create form using a .pdf file. Confirm there are form errors.
        Check file is in the form.errors keys dictionary
        Check the content of the error message is as expected.
        """
        data = {
            'added_by': User.objects.get(username='Tester'),
            'employment': Job.objects.get(employer_name='Test Company'),
            'scheme_name': 'My Pension Scheme',
            'policy_number': '124',
            'member_number': '123',
            'pension_type': 1,
            'date_joined_scheme': '2020-01-01',
            'salary': '40000',
            'pao': 'false',
            'director': 'false',
            'pension_provider': Provider.objects.get(
                provider_name='A Pension Provider'
                ),
            'value': '3000',
            'notes': '',
        }
        test_file = os.path.join(TEST_DIR, 'test-upload-pdf-file.pdf')
        with open(test_file, 'rb') as file:
            form = PensionForm(data=data, files={
                'file': SimpleUploadedFile('file', file.read())
                })
            self.assertIn('file', form.errors.keys())
        self.assertEqual(
            form.errors['file'][0],
            'File type must be .png or .jpg. Choose a different file '
            'of the correct type'
            )

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check the Meta fields attribute is equal to the list of fields
        defined in the form Meta innerclass
        """
        form = PensionForm()
        self.assertEqual(
            form.Meta.fields, [
                'employment',
                'scheme_name',
                'policy_number',
                'member_number',
                'pension_type',
                'date_joined_scheme',
                'salary',
                'pao',
                'director',
                'pension_provider',
                'value',
                'file',
                'notes',
                ]
            )
