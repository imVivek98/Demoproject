from django.contrib import admin
from django.urls import path, include

from demoapp import views

urlpatterns = [
    path('',views.home,name="name"),
    path('arithmetic/',views.arithmetic,name="arithmetic")

    #path('about/',views.about,name="about"),
    #path('contact/',views.contact,name="contact"),
    #path('details/',views.details,name="details"),
    #path('thanks/',views.thanks,name="thanks")
]
