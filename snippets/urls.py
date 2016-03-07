"""snippets/url.py."""
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'track', views.TrackViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api-root/$', views.api_root),
    url(r'^file/$', views.FileUploadView.as_view(), name='file-upload'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^profiles/', views.ProfileList.as_view(), name="profile-list"),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view(), name='profile-detail'),
    url(r'login/$', views.Login.as_view(), name="login"),
]
