# Generated by Django 3.2.5 on 2022-06-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0030_alter_appointment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='full_name',
            field=models.CharField(default='customer', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default='12346', max_length=20),
        ),
    ]