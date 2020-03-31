from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convertor


class Article(models.Model):
    STATUS_CHOICES = (
        ('P', 'منتشر شده'),
        ('D', 'در حال انتظار'),
    )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    title = models.CharField(max_length=200, verbose_name='تیتر')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images', verbose_name='عکس')
    publish = models.DateTimeField(default=timezone.now, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='به وجود امدن')
    update = models.DateTimeField(auto_now=True, verbose_name='بروزرسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "تاریخ انتشار"
