"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import renderers
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides.

     `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permissions_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """Create a custom action, named `highlight`."""
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        """Rewrite create to associating snippets with users."""
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset automatically provides `list` and `Detail` actions."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """A single entry point to our API."""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)})
