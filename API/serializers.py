from rest_framework import serializers
from Ads.models import *


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = (
            "author",
            "title",
            "body",
            "catorg",
            "category",
            "price",
            "pricerent1",
            "pricerent2",
            "pricerent3",
            "image",
            "image2",
            "sizeerth",
            "sizelot",
            "floor",
            "rooms",
            "fool",
            "services",
            "cat_city",
            "status",
            "created_at",
            "ads_vip"
        )