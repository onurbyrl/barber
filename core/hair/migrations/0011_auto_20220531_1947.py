# Generated by Django 3.2.5 on 2022-05-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0010_alter_about_about_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_us',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
    ]
