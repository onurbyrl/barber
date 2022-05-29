from django.db import models


class About(models.Model):
    title = models.CharField(max_length=999, null=True, blank=True)
    about_us = models.TextField(max_length=9999, null=True, blank=True)

    class Meta:
        verbose_name = 'Hakkımda bilgisi'
        verbose_name_plural = 'Hakkımda'

    def __str__(self):
        return self.title


class Hours(models.Model):
    hours = models.CharField(max_length=999, null=False, blank=False) # TimeField denenebilir
    # günler verilip sadece saat bilgisi de alınabilir

    class Meta:
        verbose_name = 'Saat'
        verbose_name_plural = 'Çalışma Saatleri'
        ordering = ('id',)

    def __str__(self):
        return 'Çalışma Saati'

class Contact(models.Model):
    phone = models.CharField(max_length=99, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    # social media ??

    class Meta:
        verbose_name = 'İletişim bilgisi'
        verbose_name_plural = 'İletişim Bilgileri'

    def __str__(self):
        return 'İletişim'


class Address(models.Model):
    location = models.CharField(max_length=999, null=False, blank=False)

    class Meta:
        verbose_name = 'Adres'
        verbose_name_plural = 'Adresler'

    def __str__(self):
        return self.location


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Fotoğraf'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return 'Fotograf'


class Service(models.Model):
    service = models.CharField(max_length=99, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servisler'

    def __str__(self):
        return self.service


class ServicesText(models.Model):
    first_text = models.TextField(max_length=999, null=True, blank=True)
    second_text = models.TextField(max_length=999, null=True, blank=True)

    class Meta:
        verbose_name = 'Servis yazısı'
        verbose_name_plural = 'Servis Yazılar'

    def __str__(self):
        return self.first_text