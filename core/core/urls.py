from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User, Group

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hair.urls')),
]

admin.site.site_title = 'Admin Paneli'
admin.site.name = 'Admin'
admin.site.site_header = 'Admin Paneli'
admin.site.index_title = 'Barber Shop Administration'
admin.site.unregister(User)
admin.site.unregister(Group)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)