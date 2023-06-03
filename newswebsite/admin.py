from django.contrib import admin
from newswebsite.models import Category, FlashNews, Slider, LatestNews

# Register your models here.
admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(Slider)
admin.site.register(LatestNews)
