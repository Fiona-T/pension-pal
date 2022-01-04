"""Views for the pensions app"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
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
        Display the Pension form.
        Restrict 'employment' field dropdown to jobs added by this user
        """
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

    def post(self, request):
        """
        Submit form data, redirect to success page if valid,
        else display form again (again with employment dropdown for that user)
        """
        form = PensionForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.added_by = request.user
            form.save()
            return redirect('add_pension_success')
        else:
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


class AddPensionSuccess(LoginRequiredMixin, generic.TemplateView):
    """
    Renders the success page after submitting the PensionForm from add-pension
    If not logged in, redirects to login page, then to my-jobs page
    after logging in (doesn't redirect back to success page after login)
    """
    template_name = 'add-pension-success.html'
    redirect_field_name = None


class EditPension(LoginRequiredMixin, View):
    """View for getting Edit Pension form and Posting completed form"""

    def get(self, request, pension_id):
        """
        Gets the pension by the id (passed in via the url)
        Check if the user matches the user who added the pension
        Returns the template with the form, populated with existing data
        and the Jobs added by user (for 'employment' field)
        Or raises Http404 error if the user doesn't match
        """
        pension = get_object_or_404(Pension, id=pension_id)
        if request.user == pension.added_by:
            form = PensionForm(instance=pension)
            form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
            return render(
                request,
                'edit-pension.html',
                {
                    'form': form
                }
            )
        else:
            raise Http404

    def post(self, request, pension_id):
        """
        Gets the pension by the id (passed in via the url)
        Submit form data, redirect to my-pensions page if valid,
        else display the form again on edit-pension page
        """
        pension = get_object_or_404(Pension, id=pension_id)
        form = PensionForm(request.POST, request.FILES, instance=pension)
        if form.is_valid():
            form.save()
            return redirect('my_pensions')
        else:
            form = PensionForm(instance=pension)
            form.fields['employment'].queryset = Job.objects.filter(
                added_by=request.user
                )
            return render(
                request,
                'edit-pension.html',
                {
                    'form': form
                }
            )


class DeletePension(LoginRequiredMixin, View):
    """Handles deleting a pension from delete pension modal on my-pensions"""
    def post(self, request, pension_id):
        """
        Gets pension sent via delete pension form button, deletes the pension
        Returns to the my-pensions page
        """
        pension = get_object_or_404(Pension, id=pension_id)
        pension.delete()
        return redirect('my_pensions')
