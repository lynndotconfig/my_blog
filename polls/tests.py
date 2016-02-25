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

    def test_was_published_recently_with_old_question(self):
        """Test for old question 30 days ago.

        was_published_recently() should be return False
        for question whose pub_date is 30 days ago.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_rencently_question(self):
        """Test for recently question 1 hour ago.

        was_published_recently() should be return True
        for question whose pub_date is 1 hour ago.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recently_question = Question(pub_date=time)
        self.assertEqual(recently_question.was_published_recently(), True)
