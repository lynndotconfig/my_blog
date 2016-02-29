"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """List View with get, post method."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail view with get, put, delete."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListCreateAPIView):
    """List view with get, post method."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail view with get, put, delete."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
