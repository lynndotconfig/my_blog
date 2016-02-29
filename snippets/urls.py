"""snippets/url.py."""
from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'})

user_list = views.UserViewSet.as_view({
    'get': 'list'})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'})


urlpatterns = [
    url(r'^$', snippet_list, name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api-root/$', views.api_root),
    url(r'^(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
