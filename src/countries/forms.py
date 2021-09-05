from django import forms
from .models import CountriesData

class CountryForm(forms.Form):
    countries = CountriesData.objects.values('Country').distinct()
    clist = [(c['Country'], c['Country']) for c in countries]
    clist.insert(0, ('', 'Select a country'))
    ctuple = tuple(clist)

    country_list = forms.ChoiceField(choices=ctuple, label="", required=True, 
                                     widget=forms.Select(attrs={'style': 'max-width: 300px;','class':'form-control'}))
    
class YearForm(forms.Form):
    years = CountriesData.objects.values('Year').distinct()
    ylist = [(y['Year'], y['Year']) for y in years]
    ylist.insert(0, ('', 'Select a year'))
    ytuple = tuple(ylist)
    
    year_list = forms.ChoiceField(choices=ytuple, label="", required=True, 
                                     widget=forms.Select(attrs={'style': 'max-width: 300px;','class':'form-control'}))