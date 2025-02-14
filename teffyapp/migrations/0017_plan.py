# Generated by Django 4.2.16 on 2025-01-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teffyapp', '0016_personalinformation_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('batch', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]
