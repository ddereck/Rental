from django.db import models
from django.core.validators import FileExtensionValidator
import uuid


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(null=True, blank=True, upload_to='photos', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg'])])
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    year = models.IntegerField()
    capacity = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    fuel_capacity = models.IntegerField()
    rating = models.FloatField()
    license_plate = models.CharField(max_length=20, unique=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('rented', 'Rented'), ('maintenance', 'Maintenance')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"