from django.urls import path 
from . import views 

urlpatterns = [
    path('display_loans/',views.display_loans,name='displayLoans'),
]