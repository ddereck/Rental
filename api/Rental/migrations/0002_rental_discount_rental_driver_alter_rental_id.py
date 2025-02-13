# Generated by Django 5.0.6 on 2024-07-03 16:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discount', '0002_remove_discount_users_alter_discount_id_and_more'),
        ('Rental', '0001_initial'),
        ('User', '0002_users_type_drivers'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Discount.discount'),
        ),
        migrations.AddField(
            model_name='rental',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.drivers'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
