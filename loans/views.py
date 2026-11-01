from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def display_loans(request):
    """
    loads the loans Dashboard html page
    """
    template = loader.get_template('loansDashboard.html')
    
    return HttpResponse(template.render())
