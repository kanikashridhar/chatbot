from django.test import TestCase
from django.utils import timezone

from intellibot.models import Question
from intellibot.utils import getNextQuestion
from intellibot.uservalidator import validate_gender
from intellibot.userhelper import getGender

class HelpersTest(TestCase):

   #def test_context_name(self):
   #    next_question = getNextQuestion(0)
   #    self.assertIs(next_question.question_text,"What is your name?")

    def test_validate_gender(self):
        val = validate_gender("ABC")
        self.assertIs(val,False)

        val = validate_gender("My Gender is MALE")
        self.assertIs(val,True)

        val = validate_gender("I am Female")
        self.assertIs(val,True)

        val = validate_gender("I WON'T TELL")
        self.assertIs(val,False)