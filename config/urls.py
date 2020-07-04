"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from dong import views
import dong.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dong.views.index, name='index'),
    path('main/', dong.views.main, name='main'),
    path('rap/', dong.views.rap, name='rap'),
    path('menu/', dong.views.menu, name='menu'),
    path('ballad/', dong.views.ballad, name='ballad'),
    path('song/', dong.views.song, name='song'),
    # path('index/dong/top/', views.Demo_top.as_view(), name='Demo_top'),
    path('introduction/', dong.views.introduction, name='introduction'),
    path('visitor/', dong.views.visitor, name='visitor'),
    path('recom/', dong.views.recom, name='recom'),
    path('pop/', dong.views.pop, name='pop'),

]
