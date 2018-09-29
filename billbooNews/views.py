from django.urls import reverse
from django.shortcuts import render

from apps.news.models import News, Topics


def landing(request):
    context = {}
    context['news'] = News.objects.all()
    context['topics'] = Topics.objects.all()
    return render(request, 'index.html', context)