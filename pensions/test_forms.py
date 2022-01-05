"""Unit tests for Forms for 'pensions' app"""
from django.test import TestCase
from .forms import PensionForm


class TestPensionForm(TestCase):
    """Test the Pension form - add/edit pension """

    def test_file_field_help_text(self):
        """Test that the Upload file field has the associated help text """
        form = PensionForm()
        self.assertEqual(
            form.fields['file'].help_text,
            'Upload your most recent annual benefit statement, '
            'or any other relevant file.'
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
        form = PensionForm()
        self.assertTrue(
            form.fields['salary'].label is None or
            form.fields['salary'].label == 'Salary at date of leaving service'
            )
        self.assertTrue(
            form.fields['pao'].label is None or
            form.fields['pao'].label
            == 'Is there a Pension Adjustment Order (PAO) on the pension?'
            )
        self.assertTrue(
            form.fields['director'].label is None or
            form.fields['director'].label
            == 'Were you a 20% director in this employment?'
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
        Check that each required field name key is in the keys of the form errors dict
        Check that the error returned for each empty field is correct
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
