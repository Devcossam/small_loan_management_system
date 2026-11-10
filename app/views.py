from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from loans.models import Loan


def home(request):
    """Render the home page"""
    template = loader.get_template('homePage.html')

    return HttpResponse(template.render())



def testing(request):
    """testing view"""
    template = loader.get_template('testing.html')
    mydata = Loan.objects.filter(loan_amount=1350.0).values()
    context = {
        "mydata": mydata,
    }

    return HttpResponse(template.render(context,request))
