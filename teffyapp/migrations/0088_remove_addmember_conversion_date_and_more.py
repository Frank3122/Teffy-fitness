# Generated by Django 4.2.16 on 2025-02-18 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0087_addmember_conversion_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmember',
            name='conversion_date',
        ),
        migrations.AlterField(
            model_name='addmember',
            name='select_membership_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='teffyapp.plan'),
        ),
        migrations.AlterField(
            model_name='addmember',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='teffyapp.service'),
        ),
    ]
