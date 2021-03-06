# Generated by Django 3.2.5 on 2022-05-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0011_auto_20220531_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Gallery'},
        ),
        migrations.AlterModelOptions(
            name='hours',
            options={'ordering': ('id',), 'verbose_name': 'Working hour', 'verbose_name_plural': 'Working Hours'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='servicestext',
            options={'verbose_name': 'Service Text', 'verbose_name_plural': 'Service Texts'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, help_text='e-mail address', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, help_text='phone', max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Service price', max_digits=4),
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(help_text='Service name', max_length=99),
        ),
        migrations.AlterField(
            model_name='servicestext',
            name='first_text',
            field=models.TextField(blank=True, max_length=999, null=True, verbose_name='First Text'),
        ),
        migrations.AlterField(
            model_name='servicestext',
            name='second_text',
            field=models.TextField(blank=True, max_length=999, null=True, verbose_name='Second Text'),
        ),
    ]
