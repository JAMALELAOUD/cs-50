from django.db import models
from django import forms
from .models import allhomeworks


class Homeworkform(forms.ModelForm):
    title = forms.CharField(max_length=50 , widget=forms.TextInput (attrs={'class':'','placeholder':'Enter your homework title ...'}))
    desc = forms.CharField(widget=forms.Textarea (attrs={'class':'','placeholder':'Enter your homework desc ...'}))
    image = forms.ImageField()
    class Meta:
        model = allhomeworks
        fields = '__all__'
        exclude = ('date',)