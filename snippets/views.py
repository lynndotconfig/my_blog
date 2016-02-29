"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """Snippet list view."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """Get all objects of snippets."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Update or create a record of snippets."""
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    """Detail fo snippet."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """Get all objects of snippets."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update a certain record of snippet."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete this object."""
        return self.destroy(request, *args, **kwargs)
