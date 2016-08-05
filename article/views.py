from django.shortcuts import render, redirect
from datetime import datetime
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView


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


def search_tag(request, tag):
    try:
        post_list = Article.objects.get(tag=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})


class ArticleSearchView(ListView):

    template_name = "archives.html"
    model = Article

    context_object_name = "post_list"

    def get_queryset(self):
        try:
            s = self.kwargs.get('s', None) or self.request.GET.get('s', None)
        except:
            s = ''
        if s:
            post_list = self.model.objects.filter(title__icontains=s)
        else:
            post_list = self.model.objects.all()
        return post_list


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feed/post/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'category', 'content', 'tag']
    template_name = 'article_create_form.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'category', 'content', 'tag']
    template_name = 'article_update_form.html'
