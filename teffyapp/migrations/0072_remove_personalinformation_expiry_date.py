# Generated by Django 4.2.16 on 2025-02-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0071_personalinformation_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='expiry_date',
        ),
    ]
