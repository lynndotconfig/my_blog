"""Serilizer for model snippets."""
# Create your views here.
from snippets.models import Snippet, Experiment
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer, ExperimentSerializer
from rest_framework import renderers
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, views
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from snippets.forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


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
