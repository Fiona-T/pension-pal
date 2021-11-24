"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render
from django.views import generic
# Create your views here.


class MyJobs(generic.TemplateView):
    """My Jobs page view """
    template_name = 'my-jobs.html'
