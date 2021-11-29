"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from .forms import AddJobForm


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


class AddJob(View):
    """ Add Job view handles the form to add a new job """
    def get(self, request):
        """ Get request - displays the form to add a job """
        return render(
            request,
            'add-job.html',
            {
                'form': AddJobForm()
            }
        )

    def post(self, request):
        """
        Submit form data, redirect to success page if valid,
        else display the form again
        """
        form = AddJobForm(data=request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.save()
            return redirect('my_jobs')
        else:
            form = AddJobForm()
            return render(
                request,
                'add-job.html',
                {
                    'form': AddJobForm()
                }
            )
