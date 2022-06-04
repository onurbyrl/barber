from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', null=True, blank=True)
    about_us = models.TextField(max_length=2000, verbose_name='About', null=True, blank=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class AboutImages(models.Model):
    title = models.CharField(max_length=99, verbose_name='title', null=True, blank=True)
    image = models.ImageField(upload_to='about_images/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images in About'

    def __str__(self):
        return self.title


class Hours(models.Model):
    hours = models.CharField(max_length=999, null=False, blank=False) # TimeField denenebilir
    # günler verilip sadece saat bilgisi de alınabilir

    class Meta:
        verbose_name = 'Working hour'
        verbose_name_plural = 'Working Hours'
        ordering = ('id',)

    def __str__(self):
        return 'Working Hour'

class Contact(models.Model):
    phone = models.CharField(max_length=99, help_text='phone', null=True, blank=True)
    email = models.CharField(max_length=255, help_text='e-mail address', null=True, blank=True)
    # social media ??

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return 'Contact'


class Address(models.Model):
    location = models.CharField(max_length=999, null=False, blank=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.location


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return 'Photo'


class ServicesLeft(models.Model):
    service = models.CharField(max_length=99, help_text='Service name', null=False, blank=False)
    price = models.DecimalField(max_digits=4, help_text='Service price', decimal_places=2)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services in Left'

    def __str__(self):
        return self.service


class ServicesRight(models.Model):
    service = models.CharField(max_length=99, help_text='Service name', null=False, blank=False)
    price = models.DecimalField(max_digits=4, help_text='Service price', decimal_places=2)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services in Right'

    def __str__(self):
        return self.service


class ServicesText(models.Model):
    first_text = models.TextField(max_length=99, verbose_name='First Text', null=True, blank=True)
    second_text = models.TextField(max_length=99, verbose_name='Second Text', null=True, blank=True)
    gray_text = models.TextField(max_length=99, verbose_name='Gray Text', null=True, blank=True)

    class Meta:
        verbose_name = 'Service Text'
        verbose_name_plural = 'Service Texts'

    def __str__(self):
        return self.first_text


class MotionPicture(models.Model):
    title = models.CharField(max_length=99, null=True, blank=True)
    image = models.ImageField(upload_to='motion_images/')

    class Meta:
        verbose_name = 'Motion Picture'
        verbose_name_plural = 'Motion Pictures'

    def __str__(self):
        return self.title


class Videos(models.Model):
    video = models.FileField(upload_to='videos/')
    description = models.TextField(max_length=255, verbose_name='Video description', null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return 'Video'