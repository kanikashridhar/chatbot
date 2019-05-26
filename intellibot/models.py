#Model for questions 
from django.db import models
from django.utils import timezone

class Question(models.Model):
   context = models.CharField(max_length=50)
   question_text = models.CharField(max_length=200)
   hint = models.CharField(max_length=300, default='')
   date_created = models.DateTimeField(default=timezone.now())

   def __str__(self):
      return self.question_text

   """
    def getHintForQuestion(self):
    hint_list = (Question.objects.get(pk=self.id).hint).split(":")
    print(hint_list)
    return hint_list[random.randint(0,1)]
   """
#Model for UserInformation
class UserInfo(models.Model):
    date_created = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=500)
    DOB = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    smoker = models.CharField(max_length=10)
