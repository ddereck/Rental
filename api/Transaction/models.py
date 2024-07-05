from django.db import models
from django.conf import settings
from Rental.models import Rental

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('deposit', 'Deposit'),
        ('payment', 'Payment'),
        ('refund', 'Refund'),
    ]

    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Transaction for Rental {self.rental.id} - Type: {self.type} - Amount: {self.amount}'

