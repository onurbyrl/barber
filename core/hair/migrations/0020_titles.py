# Generated by Django 3.2.5 on 2022-06-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0019_gallery_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title above videos')),
                ('gallery_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title above gallery')),
                ('services_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title above services')),
                ('hours_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title for opening hours')),
                ('contact_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title for contact')),
                ('addresses_title', models.CharField(blank=True, max_length=24, null=True, verbose_name='Title for adresses')),
            ],
            options={
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
    ]
