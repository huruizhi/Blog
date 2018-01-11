from django.urls import path, re_path
from . import views

app_name = 'blog01'
urlpatterns = [
    path('', views.index),
    re_path('detail/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    re_path('category/(?P<pk>[0-9])/', views.category, name='category'),
    re_path('tag/(?P<pk>[0-9])/', views.tag, name='tag'),
    path('index/', views.index, name='index'),
]
