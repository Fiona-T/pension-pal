"""Form for 'pensions' app to create/edit a Pension"""
from django import forms
from django.core.exceptions import ValidationError
from jobs.models import Job
from .models import Pension, Provider


class PensionForm(forms.ModelForm):
    """
    Frontend form for user to add or edit a Pension record.
    Employment field is restricted to Jobs for that user in the View.
    The dropdown lists for <select> element have selected choice set.
    Filter Providers in dropdown list to only show those with Active status (0)
    Define the class to be added to the html label element for required fields
    """
    employment = forms.ModelChoiceField(
        queryset=Job.objects.all(),
        empty_label="Choose Job the pension relates to",
        help_text='If the Job is not in the list, go to My Jobs to add the Job'
        ' record first.'
        )
    pension_provider = forms.ModelChoiceField(
        queryset=Provider.objects.filter(status=0),
        empty_label="Choose pension provider"
        )

    required_css_class = 'required-label'

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
            'salary': 'Salary at date of leaving service',
            'pao': 'Is there a Pension Adjustment Order (PAO) on the pension?',
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
            'file': 'Upload your most recent annual benefit statement, '
            'or any other relevant file.<br><strong>Note: only .jpg or .png '
            'files allowed</strong>',
            }

    def clean_file(self):
        """
        Override clean method on file field: if there is data in the field,
        check extension and raise an error for those other than png or jpg
        (as Cloudinary throws server error)
        The above raises an Atrribute Error when the Edit form submitted
        with an existing Cloudinary file, as it has no name attribute.
        Except block added to pass on an Atrribute Error. The existing
        Cloudinary file has already been checked when adding the record so
        does not need to be checked again. Anything other than this is checked
        """
        data = self.cleaned_data['file']
        if data:
            try:
                filename = data.name
                if not filename.endswith(('.jpg', '.png', '.jpeg')):
                    raise ValidationError(
                        'File type must be .png or .jpg. Choose a different '
                        'file of the correct type'
                        )
            except AttributeError:
                pass
        return data
