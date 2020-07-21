from django.shortcuts import render
from django.views.generic import ListView , DetailView 

from .models import Ads, service, category
# Create your views here.

#def index(request):
#    ads_list = Ads.objects.all()
#    context ={
#        "ads_list" : ads_list
#    }
#    return render(request , "Ads/index.html" , context)
class index(ListView):
    model = Ads
    template_name = "Ads/index.html"

class details(DetailView):
    model = Ads
    template_name = "Ads/AdsDetails.html"