"""snippets/serializers.py."""
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """Snippet serializer."""

    class Meta:
        """Meta model and fields."""

        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        """Meta model and fields."""

        model = User
        fields = ('id', 'username', 'snippets')
