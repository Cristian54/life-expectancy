from django.shortcuts import render
from .models import CountriesData
from .tables import OneCountryTable
from django_tables2 import RequestConfig

# Create your views here.
def home(request):
    ex = CountriesData.objects.all().filter(Year='1960')
    return render(request, 'home.html', context={'ex':ex})

def country(request):
    if request.method == 'GET':
        config = RequestConfig(request, paginate=False)
        USA_Data = CountriesData.objects.values('Year', 'Population', 'LifeEx').filter(Country='United States of America')
        table = OneCountryTable(USA_Data)
        config.configure(table)
        return render(request, 'country.html', {'countryData':table, 'country':'United States of America'})
    #elif request.method == 'POST':
        