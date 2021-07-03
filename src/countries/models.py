from django import db
from django.db import models

# Create your models here.
class LifeExpectancy(models.Model):
    CountryLE = models.TextField(db_column='CountryLE')  
    Year = models.TextField(db_column='Year')  
    LifeEx = models.TextField(db_column='LifeEx', blank=True)  
    dummyID = models.IntegerField(db_column='dummyID', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'LifeExpectancy'


class Populations(models.Model):
    CountryNamePop = models.TextField(db_column='CountryNamePop')  
    Year = models.TextField(db_column='Year')  
    Population = models.TextField(db_column='Population', blank=True) 
    dummyID = models.IntegerField(db_column='dummyID', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'Populations'

