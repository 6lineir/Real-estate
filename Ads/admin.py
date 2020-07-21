from django.contrib import admin
from .models import Ads, category , service
# Register your models here.

class AdsAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'status', 'category')

    
admin.site.register(Ads, AdsAdmin)
admin.site.register(category)
admin.site.register(service)