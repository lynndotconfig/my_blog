"""snippets/serializers.py."""
from rest_framework import serializers
from snippets.models import Snippet, Experiment, Profile
from snippets.models import Album, Track
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
        style={'input_type': 'password', 'placeholder': 'Password'})
    remember_me = serializers.BooleanField()
    detail = serializers.CharField(
        max_length=1000,
        style={'base_template': 'textarea.html', 'raw': 10})
    # detail_1 = serializers.CharField(
    #     max_length=1000,
    #     style={'temaplate': 'my-field-template/custom-input.html'})


class AlbumSerializer(serializers.ModelSerializer):
    """AlbumSerializer."""

    # tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tracks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='track-detail')
    tracks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')


    class Meta:
        """Meta."""

        model = Album
        fields = ('album_name', 'artist', 'tracks')


class TrackSerializer(serializers.ModelSerializer):
    """TrackSerializer."""

    class Meta:
        """Meta."""

        model = Track
        fields = ('album', 'order', 'title', 'duration')
