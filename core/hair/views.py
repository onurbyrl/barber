from django.shortcuts import render
from .models import About, Hours, Contact, Address, Gallery, Service, ServicesText

# Create your views here.

def index(request):
    about = About.objects.all()
    hours = Hours.objects.all()
    contacts = Contact.objects.all()
    addresses = Address.objects.all()
    gallery = Gallery.objects.all()
    services = Service.objects.all()
    services_texts = ServicesText.objects.all()

    return render(request, 'hair/index.html', {
        'about': about,
        'hours': hours,
        'contacts': contacts,
        'addresses': addresses,
        'gallery': gallery,
        'services': services,
        'services_texts': services_texts
    })