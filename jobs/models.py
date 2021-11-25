"""Models for the 'jobs' app (create, view, edit, delete jobs)"""
from django.db import models
from django.contrib.auth.models import User

FULL_OR_PART = ((0, 'Full-time'), (1, 'Part-time'))


class Job(models.Model):
    """ Model for Job records that user adds from frontend form """
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='jobs')
    employer_name = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    full_or_part_time = models.IntegerField(choices=FULL_OR_PART, default=0)

    class Meta:
        """order the records by employment start date in descending order"""
        ordering = ['-start_date']

    def __str__(self):
        return self.employer_name
