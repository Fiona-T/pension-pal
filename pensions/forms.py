"""Form for 'pensions' app to create/edit a Pension"""
from django import forms
from .models import Pension


class PensionForm(forms.ModelForm):
    """frontend form for user to add or edit a Pension record"""
    class Meta:
        """
        Based on Pension model, all fields except added by.
        Labels specified for some fields, helptext for file upload field.
        Widget for date fields to show format to user & include the date picker
        Date format set to yyyy-mm-dd, format displayed to user is dd/mm/yyyy
        """
        model = Pension
        fields = [
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
        labels = {
            'employment': 'Choose Employment the pension relates to',
            'salary': 'Salary at date of leaving service',
            'pao': 'Is there a Pension Adjustment Order (PAO)on the pension?',
            'director': 'Were you a 20% director in this employment?',
            'value': 'Current value of pension scheme',
            'file': 'Upload recent statement',
            'notes': 'Additional notes on this pension',
        }
        widgets = {
            'date_joined_scheme': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}),
        }
        help_texts = {
            'file': 'Upload your most recent annual benefit statement, or any other relevant file.',
            }
