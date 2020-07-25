from django.urls import path
from .views import *

app_name = "API"
urlpatterns = [
    path('v1/', AdsAPIView.as_view()),
    path('v1/<int:pk>/', AdsAPIDetail.as_view()),
]
