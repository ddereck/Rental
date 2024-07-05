
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.core.validators import FileExtensionValidator
 
class Users(AbstractUser):
    TYPE_CHOICES = [
        ('particular', 'Particular'),
        ('enterprise', 'Enterprise'),
        ('staff', 'Staff'),
    ]


    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Particular')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg'])])
    id_card_photo = models.ImageField(upload_to='id_cards', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg'])])
    driving_license_photo = models.ImageField(upload_to='driving_licenses', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg'])])
    
    def profile_completed(self):
        required_fields = [
            self.email, self.phone_number, self.address, self.city,
        ]
        return all(required_fields)
    
    groups = models.ManyToManyField(
        Group,
        related_name='users_set',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users_set',  
        blank=True,
    )

class Drivers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('User.Users', on_delete=models.CASCADE, related_name='Driver')
    availability = models.CharField(max_length=100)


    def __str__(self):
        return f'Drivers {self.id} - {self.user.first_name} {self.user.last_name} - {self.availability}' 
    