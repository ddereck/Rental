from django.db import models
from django.conf import settings
import uuid

class Discount(models.Model):
    TYPE_CHOICES = [
        ('general', 'General'),
        ('specific', 'Specific'),
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fixed_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='general')

    def __str__(self):
        return self.code


