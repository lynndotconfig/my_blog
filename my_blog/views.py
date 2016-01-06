# -*- coding: utf-8 -*-
from article.models import Article
from django.http import Http404
from django.shortcuts import render


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {
        'post_list': post_list, 'error': False})
