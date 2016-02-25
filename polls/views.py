"""views for poll model."""
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    """List the question."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the latest five published questions."""
        """(not include those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detail view of question."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    """Results view for question votes."""

    model = Question
    template_name = 'polls/results.html'


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
