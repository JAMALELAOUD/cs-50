from django.contrib import admin
from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home , name="home"),
    path('homework/',views.homeworks, name="homeworks"),
    path('homework_upload/',views.upload, name="upload"),
    path('homework/<id>/', views.homework , name="homework"),
]
