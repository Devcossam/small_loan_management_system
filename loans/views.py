from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from loans.models import Loan 

def display_loans(request):
    """
    loads the loans Dashboard html page
    """

    loans = Loan.objects.all()
    template = loader.get_template('loansDashboard.html')

    context = {
        'loans': loans,
    }
    
    return HttpResponse(template.render(context,request))


def loan_details(request,id):
    """display a particular loan's details"""

    loan = Loan.objects.get(id=id)
    template = loader.get_template('loanDetails.html')

    context = {
        'loan': loan,
    }

    return HttpResponse(template.render(context,request))




