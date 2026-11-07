from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader


def home(request):
    """Render the home page"""
    template = loader.get_template('homePage.html')

    return HttpResponse(template.render())
