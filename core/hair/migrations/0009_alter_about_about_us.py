# Generated by Django 3.2.5 on 2022-05-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0008_auto_20220531_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_us',
            field=models.TextField(blank=True, max_length=999, null=True, verbose_name='Hakkımda'),
        ),
    ]