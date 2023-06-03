from django.urls import path
from newswebsite import views
urlpatterns=[
    path('',views.HomeView.as_view(),name='home')
]