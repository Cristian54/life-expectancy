from django.shortcuts import render
from .models import LifeExpectancy, Populations

# Create your views here.
def home(request):
    ex = Populations.objects.all().filter(Year='1960')
    return render(request, 'home.html', context={'ex':ex})

def country(request):
    if request.method == 'GET':
        USA_Pop = Populations.objects.values('Population', 'Year').filter(CountryNamePop='United States of America')
        USA_LE = LifeExpectancy.objects.values('LifeEx').filter(CountryLE='United States of America')
        #for u in USA_Data: print(u)
        return render(request, 'country.html', context={'countryData':zip(USA_Pop, USA_LE), 'country':'United States of America'})
    #elif request.method == 'POST':
        