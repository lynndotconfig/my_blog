"""Test case for polls method."""
import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question
# Create your tests here.


class QuestionMethodTest(TestCase):
    """Test qeustion methods."""

    def test_was_published_recently_with_future_question(self):
        """Function test for 'was_published_recently()'.

        was_published_recently() should return False
        for question whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
