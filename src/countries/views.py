from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
import json

from .models import CountriesData
from .tables import OneCountryTable
from .forms import CountryForm

# Create your views here.
def home(request):
    YearData = CountriesData.objects.values('Country', 'Population', 'LifeEx').filter(Year='1960')
    dataDict = {"Country":[], "Population":[], "Life Expectancy":[]}
    for y in YearData: 
        dataDict['Country'].append(y['Country'])
        dataDict['Population'].append(y['Population'])
        dataDict['Life Expectancy'].append(y['LifeEx'])
    
    jsonData = json.dumps(dataDict)
    return render(request, 'home.html', {'countryData':jsonData})

def country_csv(request): 
    if request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        Country_Data = CountriesData.objects.values('Year', 'Population', 'LifeEx').filter(Country=request.POST['country_list'])
        table = OneCountryTable(Country_Data)
        config.configure(table)
        
        export_format = 'csv'
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(request.POST['country_list'] + "-Data.{}".format(export_format))

def country(request):
    if request.method == 'GET':
        config = RequestConfig(request, paginate=False)
        USA_Data = CountriesData.objects.values('Year', 'Population', 'LifeEx').filter(Country='United States of America')
        table = OneCountryTable(USA_Data)
        config.configure(table)
        
        form = CountryForm()
        
        export_format = request.GET.get("_export", None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response("USA-Data.{}".format(export_format))
        
        return render(request, 'country.html', {'countryData':table, 'country':'United States of America', 'form':form})
        
    elif request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        Country_Data = CountriesData.objects.values('Year', 'Population', 'LifeEx').filter(Country=request.POST['country_list'])
        table = OneCountryTable(Country_Data)
        config.configure(table)
        
        form = CountryForm()
        return render(request, 'country.html', {'countryData':table, 'country':request.POST['country_list'], 'form':form})
    