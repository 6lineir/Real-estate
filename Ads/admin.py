from django.contrib import admin
from .models import Ads, category , service, City
# Register your models here.

class AdsAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'status', 'catorg','category', 'cat_city')

admin.site.register(City)
admin.site.register(Ads, AdsAdmin)
admin.site.register(category)
admin.site.register(service)