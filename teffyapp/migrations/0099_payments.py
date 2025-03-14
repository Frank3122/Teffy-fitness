# Generated by Django 4.2.16 on 2025-03-04 11:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0098_delete_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.PositiveIntegerField(blank=True, null=True)),
                ('pending_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('date_paid', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name_records', to='teffyapp.personalinformation')),
                ('payments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_records', to='teffyapp.personalinformation')),
            ],
        ),
    ]
