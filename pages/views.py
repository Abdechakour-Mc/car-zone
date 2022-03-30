from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    teams = models.Team.objects.all()
    context = {"teams" : teams}
    return render(request, 'pages/home.html', context=context, )

def about(request):
    teams = models.Team.objects.all()
    context = {"teams" : teams}
    return render(request, 'pages/about.html', context= context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')