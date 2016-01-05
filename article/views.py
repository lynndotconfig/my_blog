from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from article.models import Article


# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")


def detail(request, my_args):
    post = Article.objects.all()[0]
    string = ("title=%s, category=%s, date_time=%s, content=%s" % (
        post.title, post.category, post.date_time, post.content))
    return HttpResponse(string)


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
