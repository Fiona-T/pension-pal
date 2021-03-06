"""Unit tests for Forms for 'jobs' app"""
from django.test import TestCase
from .forms import AddJobForm


class TestAddJobForm(TestCase):
    """Test the Add Job form """

    def test_finish_date_help_text(self):
        """Test that the finish date field has the associated help text """
        form = AddJobForm()
        self.assertEqual(
            form.fields['finish_date'].help_text,
            'Finish date should be after the start date.'
            )

    def test_widget_exists_on_date_fields_(self):
        """Test that the two date fields have DateInput widget attached """
        form = AddJobForm()
        self.assertEqual(
            form.fields['finish_date'].widget.__class__.__name__, 'DateInput'
            )
        self.assertEqual(
            form.fields['start_date'].widget.__class__.__name__, 'DateInput'
            )

    def test_all_fields_are_required(self):
        """
        Create a form without any details filled in, check that it is not valid
        Check that each field name key is in the keys of the form errors dict
        Check that the error returned for each empty field is correct
        """
        form = AddJobForm({
            'added_by': '',
            'employer_name': '',
            'start_date': '',
            'finish_date': '',
            'full_or_part_time': '',
        })
        self.assertFalse(form.is_valid())

        self.assertIn('employer_name', form.errors.keys())
        self.assertIn('start_date', form.errors.keys())
        self.assertIn('finish_date', form.errors.keys())
        self.assertIn('full_or_part_time', form.errors.keys())

        self.assertEqual(
            form.errors['employer_name'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['start_date'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['finish_date'][0], 'This field is required.'
            )
        self.assertEqual(
            form.errors['full_or_part_time'][0], 'This field is required.'
            )

    def test_full_or_part_time_defaults_to_full(self):
        """Check initial value on full_or_part_time is fulltime (0) """
        form = AddJobForm()
        self.assertEqual(form['full_or_part_time'].initial, 0)

    def test_finish_date_before_start_date_raises_error_message(self):
        """
        Create form instance with finish date earlier than start date, check
        it is not valid. Check that the two fields (finish and start date) are
        in the keys of the form errors dict. Check that the error returned for
        each of the two fields is correct.
        """
        form = AddJobForm({
            'added_by': 'Me',
            'employer_name': 'My Employer',
            'start_date': '2022-10-01',
            'finish_date': '2022-09-01',
            'full_or_part_time': '1',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('finish_date', form.errors.keys())
        self.assertIn('start_date', form.errors.keys())
        self.assertEqual(
            form.errors['start_date'][0],
            'Start date must be before finish date'
            )
        self.assertEqual(
            form.errors['finish_date'][0],
            'Finish date must be after start date'
            )

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check the Meta fields attribute is equal to the list of fields
        defined in the form Meta innerclass
        """
        form = AddJobForm()
        self.assertEqual(
            form.Meta.fields, [
                'employer_name',
                'start_date',
                'finish_date',
                'full_or_part_time'
                ]
            )
