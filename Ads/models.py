from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
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

class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    id = models.IntegerField(primary_key=True, unique=True, verbose_name="شناسه آگهی")
    title = models.CharField(max_length=64, verbose_name="عنوان آگهی")
    body = models.TextField(verbose_name="توضیحات")
    catorg = models.CharField(max_length=1, choices=Cat_CHOICES, verbose_name="اجاره/فروش")
    category = models.OneToOneField(category, on_delete=any , verbose_name="دسته بندی")
    price = models.IntegerField( verbose_name="ارزش کل ملک")
    pricerent1 = models.IntegerField(blank=True, verbose_name="قیمت اجاره شنبه تا چهارشنبه")
    pricerent2 = models.IntegerField(blank=True, verbose_name="قیمت اجاره چهارشنبه تا شنبه")
    pricerent3 = models.IntegerField(blank=True, verbose_name="قیمت اجاره تعطیلات")
    image = models.ImageField(upload_to="adspic", verbose_name="تصویر کاور")
    image2 = models.ImageField(upload_to="adspic", verbose_name="تصویر")
    sizeerth = models.IntegerField(blank=True, verbose_name="متراژ زمین")
    sizelot = models.IntegerField(verbose_name="متراژ بنا")
    services = models.ManyToManyField(service, blank=True, verbose_name="امکانات")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name="وضعیت فعلی" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار آگهی")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"
 