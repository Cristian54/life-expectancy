from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def country(request):
    return render(request, 'country.html')
