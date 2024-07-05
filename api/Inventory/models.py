from django.db import models
from Car.models import Car

class Inventory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    available = models.PositiveIntegerField()
    rented = models.PositiveIntegerField()
    under_maintenance = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car.make} {self.car.model} - {self.available} available out of {self.quantity}'
