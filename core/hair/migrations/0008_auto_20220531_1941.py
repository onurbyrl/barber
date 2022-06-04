# Generated by Django 3.2.5 on 2022-05-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0007_service_servicestext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Hakkımda bilgisi', 'verbose_name_plural': 'Hakkımda'},
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Adres', 'verbose_name_plural': 'Adresler'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'İletişim bilgisi', 'verbose_name_plural': 'İletişim Bilgileri'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Fotoğraf', 'verbose_name_plural': 'Galeri'},
        ),
        migrations.AlterModelOptions(
            name='hours',
            options={'ordering': ('id',), 'verbose_name': 'Saat', 'verbose_name_plural': 'Çalışma Saatleri'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Servis', 'verbose_name_plural': 'Servisler'},
        ),
        migrations.AlterModelOptions(
            name='servicestext',
            options={'verbose_name': 'Servis yazısı', 'verbose_name_plural': 'Servis Yazılar'},
        ),
        migrations.AlterField(
            model_name='about',
            name='about_us',
            field=models.TextField(blank=True, max_length=222, null=True, verbose_name='Hakkımda'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, help_text='e-mail adresi', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, help_text='telefon', max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='servis ücreti', max_digits=4),
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(help_text='servis adı', max_length=99),
        ),
    ]
