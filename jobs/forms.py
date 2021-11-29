"""Forms for the 'jobs' app - add job and edit job """
from django.forms import ModelForm
from .models import Job


class AddJobForm(ModelForm):
    """ Form for user to add a job from, Add Job button from My Jobs page """
    class Meta:
        """ Form uses the Job model """
        model = Job
        fields = [
            'employer_name', 'start_date', 'finish_date', 'full_or_part_time'
            ]
        help_texts = {
            'finish_date': ('Finish date should be after the start date.')
            }
