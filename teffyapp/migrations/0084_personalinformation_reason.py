# Generated by Django 4.2.16 on 2025-02-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0083_remove_addmember_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
