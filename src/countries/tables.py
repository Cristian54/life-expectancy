import django_tables2 as tables
from .models import CountriesData

class OneCountryTable(tables.Table):
    Population = tables.TemplateColumn(
        template_code="{% load humanize %}{{ value | intword }}"
    )
    LifeEx = tables.TemplateColumn(
        template_code = "{{ value|floatformat:2 }}", 
        verbose_name = "Life Expectancy"
    )
    class Meta:
        model = CountriesData 
        template_name = "django_tables2/bootstrap.html"
        fields = ("Year", "Population", "LifeEx")