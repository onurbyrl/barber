from django.shortcuts import render
from .models import About, AboutImages, Hours, Contact, Address, Gallery, ServicesLeft, ServicesRight, ServicesText, MotionPicture, Videos

# Create your views here.

def index(request):
    about = About.objects.all()
    about_images = AboutImages.objects.all()
    hours = Hours.objects.all()
    contacts = Contact.objects.all()
    addresses = Address.objects.all()
    gallery = Gallery.objects.all()
    services_left = ServicesLeft.objects.all()
    services_right = ServicesRight.objects.all()
    services_texts = ServicesText.objects.all()
    motion_pictures = MotionPicture.objects.all()
    videos = Videos.objects.all()

    return render(request, 'hair/index.html', {
        'about': about,
        'about_images': about_images,
        'hours': hours,
        'contacts': contacts,
        'addresses': addresses,
        'gallery': gallery,
        'services_left': services_left,
        'services_right': services_right,
        'services_texts': services_texts,
        'motion_pictures': motion_pictures,
        'videos': videos
    })