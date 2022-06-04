# Generated by Django 3.2.5 on 2022-06-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0013_motionpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(help_text='Service name', max_length=99)),
                ('price', models.DecimalField(decimal_places=2, help_text='Service price', max_digits=4)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services in Right',
            },
        ),
        migrations.RenameModel(
            old_name='Service',
            new_name='ServicesLeft',
        ),
        migrations.AlterModelOptions(
            name='servicesleft',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services in Left'},
        ),
    ]
