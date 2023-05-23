from django.contrib import admin
from newswebsite.models import Category, FlashNews, Slider, Image, SliderRepeat, LatestNews

# Register your models here.
admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(Slider)
admin.site.register(Image)
admin.site.register(SliderRepeat)
admin.site.register(LatestNews)
