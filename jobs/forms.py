"""Forms for the 'jobs' app - add job and edit job """
from django import forms
from .models import Job


class AddJobForm(forms.ModelForm):
    """ Form for user to add a job from, Add Job button from My Jobs page """
    class Meta:
        """
        Based on Job model, all fields except added by.Helptext for finish date
        Widget for date fields to show format to user, include the date picker
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
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 'type': 'date'}),
            'finish_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 'type': 'date'}),
            }
