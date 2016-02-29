"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """List View with get, post method."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail view with get, put, delete."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
