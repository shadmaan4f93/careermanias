from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('listings', views.listings, name='listings'),
    re_path(r'^coaching/$', views.coaching, name='coaching'),
]