from django.urls import path 
from . import views 

urlpatterns = [
    path('display_loans/',views.display_loans,name='displayLoans'),
    path('display_loans/loan_details/<int:id>',views.loan_details,name='loanDetails'),
]