from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.HomeView, name="home"),
    # About
    path('about', views.AboutPage, name="about"),
    # About
    path('gallery', views.GalleryPage, name="gallery"),
    # Contact
    path('contact', views.ContactPage, name="contact"),
    path('send_mail', views.send_gmail, name="send_mail"),
    # Branch
    path('branch', views.BranchPage, name="branch"),
    # Service
    path('services', views.ServicesPage, name="services"),
]
