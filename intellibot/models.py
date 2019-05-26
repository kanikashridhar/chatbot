#Model for questions 
from django.db import models
from django.utils import timezone

class Question(models.Model):
   context = models.CharField(max_length=50)
   question_text = models.CharField(max_length=200)
   date_created = models.DateTimeField(default=timezone.now())

   def __str__(self):
      return self.question_text
 
#Model for UserInformation
class UserInfo(models.Model):
    date_created = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=500)
    DOB = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    smoker = models.CharField(max_length=10)
