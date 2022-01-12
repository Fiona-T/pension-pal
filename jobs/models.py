"""Models for the 'jobs' app (create, view, edit, delete jobs)"""
from django.db import models
from django.contrib.auth.models import User

FULL_OR_PART = ((0, 'Full-time'), (1, 'Part-time'))


class Job(models.Model):
    """ Model for Job records that user adds from frontend form """
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='jobs')
    employer_name = models.CharField(max_length=40)
    start_date = models.DateField()
    finish_date = models.DateField()
    full_or_part_time = models.IntegerField(choices=FULL_OR_PART, default=0)

    class Meta:
        """
        Order the records by employment start date in descending order
        Set constraint on employer_name to be unique per user (added_by)
        """
        ordering = ['-start_date']
        constraints = [
            models.UniqueConstraint(
                fields=['added_by', 'employer_name'],
                name='unique_employer_name_per_user'
                )
        ]

    def clean_fields(self, exclude=None):
        """
        Validation on unique constraint for 'added_by' and 'employer name'
        is not done as part of .is_valid() in the view, because 'added_by'
        field is not on the form. Therefore need to call the validate_unique
        method here. Need to use clean_fields and not clean, so can specify
        not to exclude any fields, so that 'added_by' is included in the check
        """
        super().clean_fields(exclude=exclude)
        self.validate_unique()

    def __str__(self):
        return self.employer_name
