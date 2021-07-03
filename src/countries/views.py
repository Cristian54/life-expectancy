from django.shortcuts import render
from .models import LifeExpectancy, Populations

# Create your views here.
def home(request):
    ex = Populations.objects.all().filter(Year='1960')
    return render(request, 'home.html', context={'ex':ex})

def country(request):
    return render(request, 'country.html')
