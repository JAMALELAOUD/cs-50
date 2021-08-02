from django.shortcuts import render,get_object_or_404
from .models import allhomeworks
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import Homeworkform
# Create your views here.
def home(request):
    content={
        'homework': allhomeworks.objects.all(),
    }
    return render(request, 'home/index.html', content)

def homework(request, id): 
    homeworkz= get_object_or_404(allhomeworks, id=id)
    content={
        'homework': homeworkz,
    }
    return render(request, 'home/homework.html',content)

def homeworks(request):
    content={
        'homework': allhomeworks.objects.all(),
    }
    return render(request,'home/homeworks.html',content)
def upload(request):
    if request.method == 'POST':
        homework_upload(request.POST)
        if homework_upload.is_valid:
            homework_upload.save()
    else:
        homework_upload = Homeworkform()

    context={
        'Uwu':homework_upload,
    }
    return render(request, 'home/upload.html',context)