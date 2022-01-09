"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from .models import Job
from .forms import AddJobForm


class MyJobs(LoginRequiredMixin, generic.ListView):
    """
    My Jobs page view, displays list of jobs added by user, 6 jobs per page
    If user not logged in, redirects to login page, then to jobs once signed in
    handled by the LoginRequiredMixin
    """
    model = Job
    template_name = 'my-jobs.html'
    paginate_by = 6

    def get_queryset(self):
        """filter the objects by the current user"""
        return Job.objects.filter(added_by=self.request.user)


class AddJob(LoginRequiredMixin, View):
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
            return redirect('add_job_success')
        else:
            form = AddJobForm()
            return render(
                request,
                'add-job.html',
                {
                    'form': AddJobForm()
                }
            )


class AddJobSuccess(LoginRequiredMixin, generic.TemplateView):
    """
    Renders the success page after submitting the AddJobForm
    If not logged in, redirects to login page, then to jobs page as normal
    after loggin in (doesn't redirect back to success page after login)
    """
    template_name = 'add-job-success.html'
    redirect_field_name = None


class EditJob(LoginRequiredMixin, View):
    """View for displaying and posting form to edit an existing job"""

    def get(self, request, job_id):
        """
        Gets the job by the id (passed in via the url)
        Check if the user matches the user who added the job
        Returns the template with the form, populated with existing data
        Or raises Http404 error if the user doesn't match
        """
        job = get_object_or_404(Job, id=job_id)
        if request.user == job.added_by:
            return render(
                request,
                'edit-job.html',
                {
                    'form': AddJobForm(instance=job)
                }
            )
        else:
            raise Http404

    def post(self, request, job_id):
        """
        Gets the job by the id (passed in via the url)
        Submit form data, redirect to my-jobs page with success msg if valid,
        else display the form again on edit-job page
        """
        job = get_object_or_404(Job, id=job_id)
        form = AddJobForm(data=request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'Edited details for Job: "{job.employer_name}" successfully '
                'saved.'
                )
            return redirect('my_jobs')
        else:
            form = AddJobForm()
            return render(
                request,
                'edit-job.html',
                {
                    'form': AddJobForm(instance=job)
                }
            )


class DeleteJob(LoginRequiredMixin, View):
    """Handles deleting a job from delete job modal on my-jobs"""
    def get(self, request, job_id):
        """
        Get request added so that user can be redirected to 404 page
        Without this a 405 error is raised.
        """
        raise Http404

    def post(self, request, job_id):
        """
        Gets job sent via delete job form button, if job added by that
        user, deletes the job. Returns to the my-jobs page with success msg
        Otherwise raise 404 error.
        """
        job = get_object_or_404(Job, id=job_id)
        if request.user == job.added_by:
            job.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'Job: "{job.employer_name}" successfully deleted.'
                )
            return redirect('my_jobs')
        else:
            raise Http404
