# Generated by Django 4.2.16 on 2025-01-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0037_rename_return_reason_returns_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='returns',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
