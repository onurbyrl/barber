# Generated by Django 3.2.5 on 2022-05-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0005_auto_20220527_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Galeri',
            },
        ),
    ]
