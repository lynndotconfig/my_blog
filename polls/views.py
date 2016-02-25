"""views for poll model."""
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Index view for polls."""
    return HttpResponse("Hello world, you are in poll app")
