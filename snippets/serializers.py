"""snippets/serializers.py."""
from rest_framework import serializers
from snippets.models import Snippet, Experiment, Profile
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


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Example to test StaticHTMLRenderer render form."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = ('url', 'name')


class LoginSerializer(serializers.Serializer):
    """Example for test render_form parm template_pack."""

    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email'})
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placholder': 'Password'})
    remember_me = serializers.BooleanField()
