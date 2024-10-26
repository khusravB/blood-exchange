# Generated by Django 5.1.1 on 2024-09-16 20:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_donationapplication_received_amount_liters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationapplication',
            name='all_donors',
            field=models.ManyToManyField(blank=True, related_name='donation_applications_as_donor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donationapplication',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donation_applications_as_organization', to=settings.AUTH_USER_MODEL),
        ),
    ]