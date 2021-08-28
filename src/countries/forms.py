from django import forms
from .models import CountriesData


class CountryForm(forms.Form):
    countries = CountriesData.objects.values('Country').distinct()
    clist = [(c['Country'], c['Country']) for c in countries]
    clist.insert(0, ('', 'Select a country'))
    ctuple = tuple(clist)

    country_list = forms.ChoiceField(choices=ctuple, label="", required=True,
                                     widget=forms.Select(attrs={
                                            'style': 'max-width: 300px;',
                                            'class':'form-control'
                                    }))