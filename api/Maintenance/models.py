from django.db import models
from Car.models import Car

class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Maintenance for {self.car} on {self.scheduled_date}'
