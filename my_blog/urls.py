"""my_blog URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import RSSFeed
from article.views import HomeView
from article.views import DetailView
from article.views import ArchivesView
from article.views import SearchTagView
from article.views import BlogSearchView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^(?P<id>\d+)/$', DetailView().dispath(), name='detail'),
    # url(r'^archives/$', ArchivesView().as_view(), name='archives'),
    # url(r'tag(?P<tag>\w+)/$', SearchTagView().as_view(), name="search_tag"),
    # url(r'^search/$', BlogSearchView().as_view(), name="blog_search"),
    url(r'^feed/$', RSSFeed(), name="RSS"),
]
