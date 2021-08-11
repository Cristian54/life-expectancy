from django import forms
from .models import CountriesData


class CountryForm(forms.Form):
    countries = CountriesData.objects.values('Country').distinct()
    clist = [(c['Country'], c['Country']) for c in countries]
    ctuple = tuple(clist)
    
    country_list = forms.ChoiceField(choices=ctuple, widget=forms.Select, label="Select a country")