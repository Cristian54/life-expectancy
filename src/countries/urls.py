from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country', views.country, name='country'), 
    path('country/csv', view=views.country_csv, name='country/csv'), 
    path('year/csv', view=views.year_csv, name='year/csv')
]
