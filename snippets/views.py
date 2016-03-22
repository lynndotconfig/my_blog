"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet, Experiment, Profile
from snippets.models import Album, Track
from snippets.authentications import ExampleAuthentication
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.serializers import ExperimentSerializer, ProfileSerializer
from snippets.serializers import LoginSerializer, AlbumSerializer, TrackSerializer
from rest_framework import renderers
from rest_framework import authentication
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, views
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from snippets.forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status


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


class ExperimentViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides.

     `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """

    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    parser_classes = (FormParser, MultiPartParser,)

    def pre_save(self, obj):
        """File field."""
        obj.samplesheet = self.request.FILES.get('file')

    def perform_create(self, serializer):
        """Rewrite create to associating snippets with users."""
        serializer.save(user=self.request.user)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def code(self, request, *args, **kwargs):
        """Print code of experiment."""
        experiment = self.get_object()
        return Response(experiment.samplesheet)


@api_view(['GET'])
def api_root(request, format=None):
    """A single entry point to our API."""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)})


class FileUploadView(views.APIView):
    """Example to use FileUploadParser."""

    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        """Try something with upload file."""
        file_obj = request.data['file']
        return Response(status=204)


@api_view(['POST', 'GET', ])
def upload_file(request):
    """Upload file view."""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_upload_file(f):
    """Handle upload file."""
    with open('/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class ProfileList(views.APIView):
    """Example to test TemplateHTMLRenderer."""

    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        """Get list data."""
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})

    def post(self, request, format=True):
        """Add post method to create instance."""
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(views.APIView):
    """Exampel to test TemplateHTMLRenderer to render form."""

    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        """Get object."""
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        """Post object."""
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')


class Login(views.APIView):
    """Example to test render_form para template_pack."""

    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        """Get page info."""
        serializer = LoginSerializer()
        return Response({'serializer': serializer})


class AlbumViewSet(viewsets.ModelViewSet):
    """Example to test serializer stringRelatedField."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """String to test serialer stringRelatedField."""

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class Example(views.APIView):
    """Test authentications."""

    authentication_classes = (
        authentication.SessionAuthentication,
        # authentication.BasicAuthentication,
        ExampleAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """Get method."""
        import pdb; pdb.set_trace()
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }

        return Response(content)
