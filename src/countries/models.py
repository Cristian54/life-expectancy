from django import db
from django.db import models

# Create your models here.
class CountriesData(models.Model):
    Country = models.TextField(db_column='CountryName')  
    Year = models.TextField(db_column='Year')  
    LifeEx = models.TextField(db_column='LifeEx', blank=True) 
    Population = models.TextField(db_column='Population', blank=True) 
    dummyID = models.IntegerField(db_column='dummyID', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'Countries'

