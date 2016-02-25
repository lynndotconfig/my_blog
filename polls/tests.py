"""Test case for polls method."""
import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

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


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have ye to be published).
    """
   time = timezone.now() + datetime.timedelta(days=days)
   return Question.objects.create(question_text=question_text, pub_date=time) 


class QuestionViewTest(TestCase):
    """
    Test for Question views.
    """

    def test_index_view_with_no_question(self):
        """
        If no question exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be display on the
        index page.
        """
        create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Question with a pub_date in the future should not be display on
        the index page.
        """
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.", statues_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Question with pub_date in the future should not be display on the index page.
        And past one display.
        """
        create_question(question_text="Future Question", days=30)
        create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            respone.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_question(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 1.>', '<Question: Past question 2.>']
        )