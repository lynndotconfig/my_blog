"""snippets/serializers.py."""
from rest_framework import serializers
from snippets.models import Snippet, Experiment
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """Using hyperlinking between two entries."""

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        """Meta class for  snippetSerializer."""

        model = Snippet
        fields = ('url', 'highlight', 'owner', 'title',
                  'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Using hyperlinking between two entries."""

    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        """Meta class for UserSerializer."""

        model = User
        fields = ('url', 'username', 'snippets')


class ExperimentSerializer(serializers.ModelSerializer):
    """Serialize experiment."""

    code = serializers.HyperlinkedIdentityField(
        view_name='experiment-code', format='html')

    class Meta:
        """Meta class."""

        model = Experiment
        fields = ('url', 'id', 'notes', 'samplesheet', 'user', 'code')
