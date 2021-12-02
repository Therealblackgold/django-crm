from django.shortcuts import render, reverse
from .models import Package, Location
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail


def HomeView(request):
    context = {}
    return render(request, 'website/home.html', context)


def AboutPage(request):
    context = {}
    return render(request, 'website/about.html', context)


def GalleryPage(request):
    context = {}
    return render(request, 'website/gallery.html', context)


def ContactPage(request):
    context = {}
    return render(request, 'website/contact.html', context)


# Email stuff
def send_gmail(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        message_email = request.POST['message_email']
        message = request.POST['message']
        # print(name, message, message_email)

        msg_mail = str(name) + "\n" + str(message) + "\n" + str(message_email)

        send_mail(
            subject,  # subject
            msg_mail,  # message
            message_email,  # from email
            ['gautancholo@gmail.com'],  # To email
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse("Invalid request")


def BranchPage(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'website/branch.html', context)


def ServicesPage(request):
    packages = Package.objects.all()
    context = {'packages': packages}
    return render(request, 'website/services.html', context)