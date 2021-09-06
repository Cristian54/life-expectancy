from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
import json

from .models import CountriesData
from .tables import OneCountryTable, OneYearTable
from .forms import CountryForm, YearForm

# Create your views here.
def home(request):
    if request.method == 'GET': 
        config = RequestConfig(request, paginate=False)
        YearData = CountriesData.objects.values('Country', 'Population', 'LifeEx').filter(Year='1960')
        table = OneYearTable(YearData)
        config.configure(table)
        
        form = YearForm()
        
        dataDict = {"Country":[], "Population":[], "Life Expectancy":[]}
        for y in YearData: 
            dataDict['Country'].append(y['Country'])
            dataDict['Population'].append(y['Population'])
            dataDict['Life Expectancy'].append(y['LifeEx'])
        
        jsonData = json.dumps(dataDict)
        return render(request, 'home.html', {'countryData':jsonData, 'year':'1960', 'form':form, 'yearTable':table})
    
    elif request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        YearData = CountriesData.objects.values('Country', 'Population', 'LifeEx').filter(Year=request.POST['year_list'])
        table = OneYearTable(YearData)
        config.configure(table)
        
        form = YearForm()
        
        YearData = CountriesData.objects.values('Country', 'Population', 'LifeEx').filter(Year=request.POST['year_list'])
        dataDict = {"Country":[], "Population":[], "Life Expectancy":[]}
        for y in YearData: 
            dataDict['Country'].append(y['Country'])
            dataDict['Population'].append(y['Population'])
            dataDict['Life Expectancy'].append(y['LifeEx'])
        
        jsonData = json.dumps(dataDict)
        return render(request, 'home.html', {'countryData':jsonData, 'year':request.POST['year_list'], 'form':form, 'yearTable':table})

def year_csv(request): 
    if request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        Year_Data = CountriesData.objects.values('Country', 'Population', 'LifeEx').filter(Country=request.POST['year'])
        table = OneYearTable(Year_Data)
        config.configure(table)
        
        export_format = 'csv'
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(request.POST['year'] + "-Data.{}".format(export_format))

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
        return render(request, 'country.html', {'countryData':table, 'country':'United States of America', 'form':form})
        
    elif request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        Country_Data = CountriesData.objects.values('Year', 'Population', 'LifeEx').filter(Country=request.POST['country_list'])
        table = OneCountryTable(Country_Data)
        config.configure(table)
        
        form = CountryForm()
        return render(request, 'country.html', {'countryData':table, 'country':request.POST['country_list'], 'form':form})
    