"""model poll."""
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    """docstring for question."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return question_text."""
        return self.question_text

    def was_published_recently(self):
        """Check it was published recently."""
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)


class Choice(models.Model):
    """docstring for Choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return choice_text."""
        return self.choice_text
