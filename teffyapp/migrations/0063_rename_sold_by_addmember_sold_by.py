# Generated by Django 4.2.16 on 2025-01-28 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0062_addmember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmember',
            old_name='sold_by',
            new_name='sold_By',
        ),
    ]
