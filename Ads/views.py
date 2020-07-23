from django.shortcuts import render
from django.views.generic import ListView , DetailView 

from .models import Ads, service, category, City
# Create your views here.

class index(ListView):
    model = Ads
    template_name = "Ads/index.html"

class details(DetailView):
    model = Ads
    template_name = "Ads/AdsDetails.html"