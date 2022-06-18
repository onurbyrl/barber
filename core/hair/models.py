from django.db import models
from django.core.validators import MinLengthValidator


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', null=True, blank=True)
    about_us = models.TextField(max_length=2000, validators=[MinLengthValidator(100)], verbose_name='About', null=True, blank=True)

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


class TopImage(models.Model):
    title = models.CharField(max_length=99, verbose_name='title', default='Main Image at top of the website', null=True, blank=True)
    image = models.ImageField(upload_to='main_image/')

    class Meta:
        verbose_name = 'Main Image'
        verbose_name_plural = 'Main Image'

    def __str__(self):
        return self.title


class Hours(models.Model):
    hours = models.CharField(max_length=99, help_text='ex: Monday-Friday: 08.00-18.30', null=False, blank=False)

    class Meta:
        verbose_name = 'Working hour'
        verbose_name_plural = 'Working Hours'
        ordering = ('id',)

    def __str__(self):
        return 'Working Hour'

class Contact(models.Model):
    phone = models.CharField(max_length=99, help_text='phone', null=True, blank=True)
    email = models.CharField(max_length=99, help_text='e-mail address', null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return 'Contact'


class Address(models.Model):
    location = models.CharField(max_length=99, null=False, blank=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.location


class Gallery(models.Model):
    title = models.CharField(max_length=99, null=True, blank=True)
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
    gray_text = models.TextField(max_length=99, verbose_name='Gray Small Text', null=True, blank=True)

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
    description = models.TextField(max_length=200, verbose_name='Video description', null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return 'Video'


class Titles(models.Model):
    videos_title = models.CharField(max_length=24, verbose_name='Title above videos', null=True, blank=True)
    gallery_title = models.CharField(max_length=24, verbose_name='Title above gallery', null=True, blank=True)
    services_title = models.CharField(max_length=24, verbose_name='Title above services', null=True, blank=True)
    hours_title = models.CharField(max_length=24, verbose_name='Title for opening hours', null=True, blank=True)
    contact_title = models.CharField(max_length=24, verbose_name='Title for contact', null=True, blank=True)
    addresses_title = models.CharField(max_length=24, verbose_name='Title for adresses', null=True, blank=True)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return ''