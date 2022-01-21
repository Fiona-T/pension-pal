"""Views for the pensions app"""
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from jobs.models import Job
from .forms import PensionForm
from .models import Pension, Provider


class MyPensions(LoginRequiredMixin, generic.ListView):
    """My Pensions page view"""
    model = Pension
    template_name = 'my-pensions.html'
    paginate_by = 6

    def get_queryset(self):
        """filter the objects by the current user"""
        return Pension.objects.filter(added_by=self.request.user)


class PensionDetails(LoginRequiredMixin, View):
    """Display full pension details including linked Job + Provider details"""
    def get(self, request, pension_id):
        """
        get the pension by the id passed via url, get the linked job + pension
        provider by their ids, pass these as context and render the template
        If the user did not add this pension record, then raise Http404 error
        """
        pension = get_object_or_404(Pension, id=pension_id)
        job = get_object_or_404(Job, id=pension.employment_id)
        provider = get_object_or_404(Provider, id=pension.pension_provider_id)
        if request.user == pension.added_by:
            return render(
                request,
                "view-pension.html",
                {
                    'pension': pension,
                    'job': job,
                    'provider': provider,
                }
            )
        else:
            raise Http404


class AddPension(LoginRequiredMixin, View):
    """Add pension view - display form on get request, post form on post req"""
    def get(self, request):
        """
        Get the jobs added by the user, and if these exist then:
        Display the Pension form, restricting the 'employment' field dropdown
        to jobs added by this user.
        If user has no job records, then just return the html page (template
        displays a message informing the user they must add a Job first).
        """
        if Job.objects.filter(added_by=self.request.user):
            form = PensionForm()
            form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
            return render(
                request,
                'add-pension.html',
                {
                    'form': form
                }
            )
        else:
            return render(request, 'add-pension.html',)

    def post(self, request):
        """
        Submit form data, redirect to success page if valid,
        else display form again (again with employment dropdown for that user)
        """
        form = PensionForm(request.POST, request.FILES)
        form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
        if form.is_valid():
            form.instance.added_by = request.user
            pension = form.save()
            return redirect(reverse('add_pension_success', args=[pension.id]))
        else:
            return render(request, 'add-pension.html', {'form': form})


class AddPensionSuccess(LoginRequiredMixin, View):
    """
    View for success page after adding a pension
    If not logged in, redirects to login page, then to my-jobs page
    after logging in (doesn't redirect back to success page after login)
    """
    redirect_field_name = None

    def get(self, request, pension_id):
        """
        Renders success page after submitting the PensionForm from add-pension.
        Contains link to view the full pension details just submitted
        If pension id in url was not added by the user, raise 404 error
        """
        pension = get_object_or_404(Pension, id=pension_id)
        if pension.added_by == request.user:
            return render(
                request, 'add-pension-success.html', {'pension': pension}
                )
        else:
            raise Http404


class EditPension(LoginRequiredMixin, View):
    """View for getting Edit Pension form and Posting completed form"""

    def get(self, request, pension_id):
        """
        Gets the pension by the id (passed in via the url)
        Get the associated job (so edit job link has the job id)
        Check if the user matches the user who added the pension
        Returns the template with the form, populated with existing data
        and the Jobs added by user (for 'employment' field)
        Or raises Http404 error if the user doesn't match
        """
        pension = get_object_or_404(Pension, id=pension_id)
        job = get_object_or_404(Job, id=pension.employment_id)
        if request.user == pension.added_by:
            form = PensionForm(instance=pension)
            form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
            return render(
                request,
                'edit-pension.html',
                {
                    'form': form,
                    'job': job,
                }
            )
        else:
            raise Http404

    def post(self, request, pension_id):
        """
        Gets the pension by the id (passed in via the url)
        Get the associated job (so edit job link has the job id)
        Submit form data, redirect to my-pensions page with msg if valid,
        else display the form again on edit-pension page
        """
        pension = get_object_or_404(Pension, id=pension_id)
        job = get_object_or_404(Job, id=pension.employment_id)
        form = PensionForm(request.POST, request.FILES, instance=pension)
        form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'Edited details for Pension: "{pension.scheme_name}" for '
                f'"{pension.employment}" successfully saved.'
                )
            return redirect('my_pensions')
        else:
            return render(
                request,
                'edit-pension.html',
                {
                    'form': form,
                    'job': job,
                }
            )


class DeletePension(LoginRequiredMixin, View):
    """Handles deleting a pension from delete pension modal on my-pensions"""

    def get(self, request, pension_id):
        """
        Get request added so that user can be redirected to 404 page
        Without this a 405 error is raised.
        """
        raise Http404

    def post(self, request, pension_id):
        """
        Gets pension sent via delete pension form button, if the pension was
        added by that user, deletes the pension and returns to the my-pensions
        page with a success flash message.
        Otherwise raises 404 error.
        """
        pension = get_object_or_404(Pension, id=pension_id)
        if request.user == pension.added_by:
            pension.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'Pension: "{pension.scheme_name}" for "{pension.employment}" '
                'successfully deleted.'
                )
            return redirect('my_pensions')
        else:
            raise Http404
