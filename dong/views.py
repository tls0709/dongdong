from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, MonthArchiveView, DayArchiveView, \
    YearArchiveView
from dong.models import Post
# Create your views here.

class Demo_top(View):
    def get(self, request):
        return render(request, 'dong/top.html')


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def rap(request):
    return render(request, 'rap.html')


def menu(request):
    return render(request, 'menu.html')


def ballad(request):
    return render(request, 'ballad.html')


def top(request):
    return render(request, 'top.html')


def introduction(request):
    return render(request, 'introduction.html')


def song(request):
    return render(request, 'song.html')


def recom(request):
    return render(request, 'recom.html')


def pop(request):
    return render(request, 'pop.html')


def visitor(request):
    return render(request, 'visitor.html')


def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {
        'post': post,
    })