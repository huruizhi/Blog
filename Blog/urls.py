"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog01 import views
from blog01.feeds import AllPostsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index),
    re_path('detail/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    re_path('category/(?P<pk>[0-9])/', views.category, name='category'),
    re_path('tag/(?P<pk>[0-9])/', views.tag, name='tag'),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
]
