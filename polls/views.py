"""views for poll model."""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    """Index view for polls."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Detail view for poll."""
    obj = Question.objects.get(id=question_id)
    context = {
        'object': obj,
    }
    return render(request, 'polls/detail.html', context)


def result(request, question_id):
    """Result view for polls."""
    return HttpResponse("Yor're looking at result of %s" % question_id)


def vote(request, question_id):
    """Vote for poll."""
    return HttpResponse("Your are voting on question %s" % question_id)
