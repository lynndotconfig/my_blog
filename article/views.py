from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.views.generic import ListView


class ArticleListView(ListView):
    model = Article
    template_name = "home.html"

    paginate_by = 3
    context_object_name = "post_list"


class ArticleDetailView(DetailView):

    model = Article
    template_name = "post.html"


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {
        'post_list': post_list, 'error': False})


def search_tag(request):
    return render(request, 'home.html')


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        post_list = Article.objects.filter(title__icontains=s)
        if len(post_list) == 0:
            return render(request, 'archives.html', {'post_list': post_list,
                                                     'error': True})
        return render(request, 'archives.html', {'post_list': post_list,
                                                 'error': False})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feed/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content
