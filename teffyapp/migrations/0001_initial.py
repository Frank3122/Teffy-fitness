# Generated by Django 4.2.16 on 2024-12-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('occupation', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('perfect_body', models.CharField(blank=True, max_length=20, null=True)),
                ('body_type', models.CharField(blank=True, max_length=20, null=True)),
                ('goal', models.CharField(blank=True, max_length=30, null=True)),
                ('body_you_want', models.CharField(blank=True, max_length=50, null=True)),
                ('level_of_body_fat', models.CharField(blank=True, max_length=50, null=True)),
                ('problem_areas', models.CharField(blank=True, max_length=50, null=True)),
                ('diets', models.CharField(blank=True, max_length=70, null=True)),
                ('water_you_drink_daily', models.CharField(blank=True, max_length=50, null=True)),
                ('eat_or_dividie_foods_or_beverages', models.CharField(blank=True, max_length=70, null=True)),
                ('programe', models.CharField(blank=True, max_length=50, null=True)),
                ('event_coming_up', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(max_length=50)),
                ('current_weight', models.CharField(max_length=50)),
                ('target_weight', models.CharField(max_length=50)),
                ('level_of_fitness', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]