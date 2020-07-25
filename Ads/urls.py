from django.urls import path
from .views import *

app_name = "Ads"
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('ads/<int:pk>/', details.as_view(), name='AdsDetails'),
]
