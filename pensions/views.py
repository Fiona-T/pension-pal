"""Views for the pensions app"""
from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PensionForm


class MyPensions(generic.TemplateView):
    """My Pensions page view"""
    template_name = 'my-pensions.html'


class AddPension(LoginRequiredMixin, View):
    """Add pension view - display form on get request, post form on post req"""
    def get(self, request):
        """Display the form"""
        return render(
            request,
            'add-pension.html',
            {
                "form": PensionForm()
            }
        )
