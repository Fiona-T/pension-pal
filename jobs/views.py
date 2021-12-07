"""Views for the 'jobs' app (create, view, edit, delete jobs)"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
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
        Returns the template with the form, populated with existing data
        """
        job = get_object_or_404(Job, id=job_id)
        return render(
            request,
            'edit-job.html',
            {
                'form': AddJobForm(instance=job)
            }
        )

    def post(self, request, job_id):
        """
        Gets the job by the id (passed in via the url)
        Submit form data, redirect to my-jobs page if valid,
        else display the form again on edit-job page
        """
        job = get_object_or_404(Job, id=job_id)
        form = AddJobForm(data=request.POST, instance=job)
        if form.is_valid():
            form.save()
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
    def post(self, request, job_id):
        """
        Gets job sent via delete job form button, deletes the job
        Returns to the my-jobs page
        """
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('my_jobs')
