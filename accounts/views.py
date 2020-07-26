from django.shortcuts import render
from .models import User
from Ads.models import Ads
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView
)

class dash(ListView):
    model = Ads
    template_name = "panel/index.html"
class Ads_list(LoginRequiredMixin, ListView):
    model = Ads
    template_name = "panel/Ads-list.html"

class profile(LoginRequiredMixin ,UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:profile")
    template_name = "panel/profile.html"

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
		})
        return kwargs
class Ads_add(LoginRequiredMixin ,CreateView):
    model = Ads
    template_name = "panel/Ads-add.html"