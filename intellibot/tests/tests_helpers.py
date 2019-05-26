from django.test import TestCase
from django.utils import timezone

from intellibot.models import Question
from intellibot.utils import getNextQuestion
from intellibot.uservalidator import validate_gender , validate_smoker , validate_DOB

class HelpersTest(TestCase):

   #def test_context_name(self):
   #    next_question = getNextQuestion(0)
   #    self.assertIs(next_question.question_text,"What is your name?")

    def test_validate_gender(self):
        val = validate_gender("ABC")
        self.assertEqual(val,False)

        val = validate_gender("My Gender is MALE")
        self.assertEqual(val,True)

        val = validate_gender("I am Female")
        self.assertEqual(val,True)

        val = validate_gender("I WON'T TELL")
        self.assertEqual(val,False)

    def test_validate_smoker(self):
        val = validate_smoker("YES I AM A SMOKER")
        self.assertEqual(val,True)
        
        val = validate_smoker("NO")
        self.assertEqual(val,True)

        val = validate_smoker("ABC")
        self.assertEqual(val,False)    

    def test_validate_DOB(self):
        val = validate_DOB("My DOB is 04-08-1986")
        self.assertEqual(val,True)
        
        val = validate_DOB("DOB:04-08-2020")
        self.assertEqual(val,False)

        val = validate_DOB("04-15-1988")
        self.assertEqual(val,False)   

        val = validate_DOB("34-03-1988")
        self.assertEqual(val,False) 
