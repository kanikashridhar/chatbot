from django.test import TestCase
from django.utils import timezone

from intellibot.userhelper import getGender,getSmoker,getDOB

class HelpersTest(TestCase):

   #def test_context_name(self):
   #    next_question = getNextQuestion(0)
   #    self.assertIs(next_question.question_text,"What is your name?")

    def test_get_gender(self):
        val = getGender("MALE")
        self.assertIs(val,"Male")

        val = getGender("FEMALE")
        self.assertIs(val,"Female")

        val = getGender("LADY")
        self.assertIs(val,"Female")
       
    
    def test_get_smoker(self):
        val = getSmoker("YES I AM A SMOKER")
        self.assertEqual(val,"Smoker")
        
        val = getSmoker("NO")
        self.assertEqual(val,"Non-Smoker")

        val = getSmoker("NOT")
        self.assertEqual(val,"Non-Smoker")


    def test_get_DOB(self):
        val = getDOB("My DOB is 04-08-1986")
        self.assertEqual(val,'04-08-1986')

        val = getDOB("My DOB is")
        self.assertEqual(val,False)