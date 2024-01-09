from django.shortcuts import render
from .models import Specialty
# Create your views here.
def home_view(request):
    specialties = Specialty.objects.all()
    return render (request, 'home.html', context ={'specialties' : specialties} )
