from django.shortcuts import render
from .models import allhomeworks
from django.contrib import messages
from django.utils.translation import gettext as _
# Create your views here.
def home(request):
    content={
        'homework': allhomeworks.objects.all(),
    }
    return render(request, 'home/index.html', content)

def homework(request, id): 
    content={
        'homework': allhomeworks.objects.all(),
    }
    return render(request, 'home/homework.html')

def homeworks(request):
    return render(request,'home/homeworks.html',content)