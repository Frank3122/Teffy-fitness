# Generated by Django 4.2.16 on 2025-01-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0021_rename_price_service_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='users', to='teffyapp.service'),
        ),
    ]