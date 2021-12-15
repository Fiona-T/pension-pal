"""Views for the pensions app"""
from django.shortcuts import render
from django.views import generic


class MyPensions(generic.TemplateView):
    """My Pensions page view"""
    template_name = 'my-pensions.html'
