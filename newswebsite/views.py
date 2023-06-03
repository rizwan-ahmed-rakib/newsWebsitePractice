from django.shortcuts import render
from django.views.generic import TemplateView
from newswebsite.models import Category, Slider, FlashNews, LatestNews


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['sliders'] = Slider.objects.all()
        context['letestNews'] = LatestNews.objects.all()
        return context
