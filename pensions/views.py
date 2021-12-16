"""Views for the pensions app"""
from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import Job
from .forms import PensionForm
from .models import Pension


class MyPensions(LoginRequiredMixin, generic.ListView):
    """My Pensions page view"""
    model = Pension
    template_name = 'my-pensions.html'
    paginate_by = 6

    def get_queryset(self):
        """filter the objects by the current user"""
        return Pension.objects.filter(added_by=self.request.user)


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
                "form": form
            }
        )
