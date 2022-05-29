from django.urls import path
from . import views

app_name = 'hair'

urlpatterns = [
    path('', views.index, name='index'),
]