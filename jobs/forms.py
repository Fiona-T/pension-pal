"""Forms for the 'jobs' app - add job and edit job """
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from .models import Job


class AddJobForm(forms.ModelForm):
    """ Form for user to add or edit a job from My Jobs page """
    class Meta:
        """
        Based on Job model, all fields except added by.Helptext for finish date
        Widget for date fields to show format to user & include the date picker
        Date format set to yyyy-mm-dd, format displayed to user is dd/mm/yyyy
        Custom error message for unique constraint on employer_name per user.
        """
        model = Job
        fields = [
            'employer_name', 'start_date', 'finish_date', 'full_or_part_time'
            ]
        help_texts = {
            'finish_date': ('Finish date should be after the start date.')
            }
        widgets = {
            'start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}),
            'finish_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}),
            }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'You already have a Job with this Employer'
                ' name. Choose a different name for this new Job record.'
            }
        }

    def clean(self):
        """
        Override the clean method on the form to include a check that finish
        date is not before the start date (if both fields first have data).
        Raise errors on the two fields if it is.
        """
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        finish_date = cleaned_data.get('finish_date')

        if finish_date and start_date:
            if finish_date < start_date:
                self.add_error(
                    'finish_date',
                    ValidationError('Finish date must be after start date')
                    )
                self.add_error(
                    'start_date',
                    ValidationError('Start date must be before finish date')
                    )
