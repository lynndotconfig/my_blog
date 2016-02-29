"""snippets/url.py."""
from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers


user_list = views.UserViewSet.as_view({
    'get': 'list'})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'})

urlpatterns = [
    url(r'^$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api-root/$', views.api_root),
    url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
