from django.db import transaction
from django.core.management.base import BaseCommand
from User.models import Users

class Seeder:
    @classmethod
    def seedSuperAdmin(cls):
    
        
        super_email = input("Enter super user email:")
        super_password = input("Enter super user password:")

        with transaction.atomic():
            super_user, created = Users.objects.get_or_create(
                email=super_email,
                defaults={
                    'first_name': 'Super',
                    'last_name': 'Admin',
                    'phone_number': '00000001',
                }
            )

            if created:
                super_user.set_password(super_password)
                super_user.save()
            
            print (f"Message: Success, [Email: {super_email}, Password: **********]")

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding Super Admin...')
        Seeder.seedSuperAdmin()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the Super Admin'))
