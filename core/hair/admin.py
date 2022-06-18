from django.contrib import admin
from .models import About, AboutImages, Address, Contact, Gallery, Hours, MotionPicture, ServicesLeft, ServicesRight, ServicesText, Titles, TopImage, Videos


TEXT = 'Write the title'
TEXT2 = 'Write the paragraph about you'

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_us')
    # fieldsets = (
    #     ('Hakkımda Başlık', {
    #         'fields': ('title',),
    #         'description': '%s' %TEXT,
    #     }),
    #     ('Hakkımda İçerik', {
    #         'fields': ('about_us',),
    #         'description': '%s' %TEXT2,
    #     }),
    # )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutImages)
class AboutImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TopImage)
class TopImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    list_display = ('hours',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')

    def has_add_permission(self, request):
        return False


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('location',)
    ordering = ('id',)
    fieldsets = (
        ('Write the location info', {
            'fields': ('location',),
            'description': '',
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(ServicesLeft)
class ServicesLeftAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    ordering = ('id',)


@admin.register(ServicesRight)
class ServicesRightAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    ordering = ('id',)


@admin.register(ServicesText)
class ServicesTextAdmin(admin.ModelAdmin):
    list_display = ('first_text', 'second_text', 'gray_text')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MotionPicture)
class MotionPictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('video', 'description')


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ('videos_title', 'gallery_title', 'services_title', 'hours_title', 'contact_title', 'addresses_title')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False