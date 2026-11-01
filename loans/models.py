from django.db import models

class Loan(models.Model):
    customer_name = models.CharField(max_length=100)
    loan_amount = models.FloatField()
    created_on_date = models.DateField(null=True)