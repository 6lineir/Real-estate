from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns +=[
    path('', dash.as_view(), name='dashboard'),
    path('profile/', profile.as_view(), name='profile'),
    path('adslist/', Ads_list.as_view(), name='Adslist'),
    path('adsadd/', Ads_add.as_view(), name='Adsadd'),
]