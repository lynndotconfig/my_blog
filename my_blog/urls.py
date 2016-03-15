"""my_blog URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article.views import RSSFeed, ArticleDetailView, ArticleListView, ArticleSearchView, ArticleCreateView
from article.views import ArticleUpdateView


urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^$', 'article.views.home'),
    # url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    # url(r'^test/$', 'article.views.test'),
    url(r'^$', ArticleListView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    # url(r'^archives/$', 'article.views.archives', name='archives'),
    # url(r'tag/(?P<tag>\w+)/$', 'article.views.search_tag', name="search_tag"),
    url(r'^search/$', ArticleSearchView.as_view(), name="blog_search"),
    url(r'^feed/$', RSSFeed(), name="RSS"),
    url(r'^create/$', ArticleCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name="update"),
]
