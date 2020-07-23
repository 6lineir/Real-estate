from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class City(models.Model):
    ct_title = models.CharField(max_length=48, verbose_name='استان')
    
    def __str__(self):
        return self.ct_title
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"

class category(models.Model):
    cat_title = models.CharField(max_length=48, verbose_name='دسته بندی')
    cat_slug = models.SlugField(verbose_name='لینک دسته بندی') 
    
    def __str__(self):
        return self.cat_title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class service(models.Model):
    sr_title = models.CharField(max_length=48, verbose_name='امکانات')
    
    def __str__(self):
        return self.sr_title
    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

STATUS_CHOICES = (
        ('R', "اجاره شده"),
        ('N', "خالی شده"),
	)
Cat_CHOICES = (
        ('R', "برای اجاره"),
        ('S', "برای فروش"),
	)
Room_CHOICES = (
        ('1', "تک خواب"),
        ('2', "دو خواب"),
        ('3', "سه خواب"),
        ('4', "چهار خواب"),
        ('5', "پنج به بالا"),
	)
Floor_CHOICES = (
        ('1', "همکف"),
        ('2', "دو طبقه"),
        ('3', "سه طبقه"),
        ('4', "چهار طبقه"),
        ('5', "پنج طبقه به بالا"),
	)
Fool_CHOICES = (
        ('2', "دو نفر"),
        ('4', "چهار نفر"),
        ('5', "پنج نفر"),
        ('6', "شش نفر"),
        ('8', "هشت نفر"),
        ('10', "ده نفر"),
        ('15', "پانزده به بالا"),
	)

class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    title = models.CharField(max_length=64, verbose_name="عنوان آگهی")
    body = models.TextField(verbose_name="توضیحات")
    catorg = models.CharField(max_length=1, choices=Cat_CHOICES, verbose_name="اجاره/فروش")
    category = models.ForeignKey(category,on_delete=any, verbose_name="دسته بندی")
    price = models.IntegerField(blank=True, null=True, verbose_name="قیمت فروش ملک")
    pricerent1 = models.IntegerField(blank=True, null=True, verbose_name="قیمت اجاره شنبه تا چهارشنبه")
    pricerent2 = models.IntegerField(blank=True, null=True, verbose_name="قیمت اجاره چهارشنبه تا شنبه")
    pricerent3 = models.IntegerField(blank=True, null=True, verbose_name="قیمت اجاره تعطیلات")
    image = models.ImageField(upload_to="adspic", verbose_name="تصویر کاور")
    image2 = models.ImageField(upload_to="adspic", verbose_name="تصویر")
    sizeerth = models.IntegerField(blank=True, verbose_name="متراژ زمین")
    sizelot = models.IntegerField(verbose_name="متراژ بنا")
    floor = models.CharField(max_length=2, choices=Floor_CHOICES, blank=True, verbose_name="تعداد طبقات")
    rooms = models.CharField(max_length=1, choices=Room_CHOICES, blank=True, verbose_name="تعداد اتاق خواب")
    fool = models.CharField(max_length=2, choices=Fool_CHOICES, blank=True, verbose_name="ظرفیت نفرات")
    services = models.ManyToManyField(service, blank=True, verbose_name="امکانات")
    cat_city = models.ForeignKey(City,on_delete=any, verbose_name="استان")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name="وضعیت فعلی" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار آگهی")
    ads_vip = models.BooleanField(default=False, verbose_name="آگهی ویژه")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"
 