# Generated by Django 4.2.16 on 2024-12-14 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0003_delete_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='programe',
        ),
    ]
