# Generated by Django 4.2.16 on 2025-02-19 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0089_remove_addmember_converted_from_lead_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmember',
            name='sold_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teffyapp.userprofile'),
        ),
    ]
