import django_tables2 as tables
from .models import CountriesData

class OneCountryTable(tables.Table):
    Population = tables.TemplateColumn(
        template_code="{% load humanize %}{{ value | intword }}",
        initial_sort_descending=True
    )
    LifeEx = tables.TemplateColumn(
        template_code = "{{ value|floatformat:2 }}", 
        verbose_name = "Life Expectancy",
        initial_sort_descending=True
    )
    Year = tables.Column(initial_sort_descending=True)
    class Meta:
        model = CountriesData 
        template_name = "django_tables2/bootstrap.html"
        fields = ("Year", "Population", "LifeEx")
        attrs = {'class': 'table table-striped table-hover',
                 'id': 'countryTable'}