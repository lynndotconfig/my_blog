from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from article.models import Article
from django.http import Http404


# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.ojects.get(id=str(id))
    except Article.DoseNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
