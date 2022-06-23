from django.shortcuts import render
from django.http import HttpResponse
from .models import About, AboutImages, Titles, TopImage, Hours, Contact, Address, Gallery, ServicesLeft, ServicesRight, ServicesText, MotionPicture, Videos, Appointment
from django.contrib import messages

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
    top_image = TopImage.objects.all()
    titles = Titles.objects.all()
    

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
        'videos': videos,
        'top_image': top_image,
        'titles': titles
    })


def appointment(request):

    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        date_time = request.POST['date_time']
        
        Appointment.objects.create(full_name=full_name, phone=phone, date_time=date_time)

        messages.success(request, 'There is a new appointment!')

        return HttpResponse("Your appointment has succesfully created!")


    return render(request, 'hair/appointment.html', {})