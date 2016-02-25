"""views for poll model."""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


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
    obj = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': obj})


def result(request, question_id):
    """Result view for polls."""
    return HttpResponse("Yor're looking at result of %s" % question_id)


def vote(request, question_id):
    """Vote for poll."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting from
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data, This prevents data being posted twice
        # if a user hit the Back button
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,)))
    finally:
        pass
    return HttpResponse("Your are voting on question %s" % question_id)
