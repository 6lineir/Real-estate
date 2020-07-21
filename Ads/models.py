from django.db import models
from accounts.models import User

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

class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    id = models.IntegerField(primary_key=True, unique=True, verbose_name="کد آگهی")
    title = models.CharField(max_length=64, verbose_name="عنوان آگهی")
    body = models.TextField(verbose_name="توضیحات")
    category = models.OneToOneField(category, on_delete=any , verbose_name="دسته بندی")
    price1 = models.DecimalField(max_digits=17, decimal_places=3, verbose_name="ارزش کل ملک")
    price2 = models.DecimalField(max_digits=17, decimal_places=3, blank=True, verbose_name="قیمت اجاره شنبه تا چهارشنبه")
    price3 = models.DecimalField(max_digits=17, decimal_places=3, blank=True, verbose_name="قیمت اجاره چهارشنبه تا شنبه")
    image = models.ImageField(upload_to="adspic", verbose_name="تصویر کاور")
    image2 = models.ImageField(upload_to="adspic", verbose_name="تصویر")
    size1 = models.IntegerField(verbose_name="متراژ زمین")
    size2 = models.IntegerField(verbose_name="متراژ بنا")
    #room= 
    services = models.ManyToManyField(service, verbose_name="امکانات")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت فعلی" )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"
 