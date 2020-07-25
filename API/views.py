from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import AdsSerializer
from Ads.models import *
# Create your views here.
class AdsAPIView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AdsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer