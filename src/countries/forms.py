from django import forms
from .models import CountriesData


class CountryForm(forms.Form):
    countries = CountriesData.objects.values('Country').distinct()
    clist = [c['Country'] for c in countries]
    numberedList = [(n, c) for (n, c) in zip(range(len(clist)), clist)]
    ctuple = tuple(numberedList)
    
    country_list = forms.ChoiceField(choices=ctuple, widget=forms.Select)