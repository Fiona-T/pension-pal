"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render
from django.views import generic
from .models import Job


class MyJobs(generic.ListView):
    """My Jobs page view, displays list of jobs added by user"""
    model = Job
    template_name = 'my-jobs.html'

    def get_queryset(self):
        """filter the objects by the current user"""
        return Job.objects.filter(added_by=self.request.user)
