"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job


class MyJobs(LoginRequiredMixin, generic.ListView):
    """
    My Jobs page view, displays list of jobs added by user
    If user not logged in, redirects to login page, then to jobs once signed in
    handled by the LoginRequiredMixin
    """
    model = Job
    template_name = 'my-jobs.html'

    def get_queryset(self):
        """filter the objects by the current user"""
        return Job.objects.filter(added_by=self.request.user)
