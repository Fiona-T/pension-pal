"""Views for the 'pages' app (static pages)"""
from django.shortcuts import render
from django.views import generic

# Create your views here.


class HomePage(generic.TemplateView):
    """Home Page view - static page, no model"""
    template_name = 'index.html'
