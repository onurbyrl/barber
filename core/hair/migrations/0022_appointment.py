# Generated by Django 3.2.5 on 2022-06-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0021_auto_20220618_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('date', models.DateField(unique=True)),
                ('time', models.TimeField(unique=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]