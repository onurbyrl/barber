from django.contrib import admin
from .models import About, Address, Contact, Gallery, Hours, Service, ServicesText

# registering models to admin panel

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_us')


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    list_display = ('hours',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('location',)
    ordering = ('id',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    ordering = ('id',)


@admin.register(ServicesText)
class ServicesTextAdmin(admin.ModelAdmin):
    list_display = ('first_text', 'second_text')