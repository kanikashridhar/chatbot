import json
from intellibot.models import Question, UserInfo
from intellibot.uservalidator import validateUserResponse
import datetime, re

def createMessage(text, command, source):
    return {
        'text': text,
        'type': 'text',
        'command': command,
        'source': source
    }

def createBotMessage(text, command, mid, context):
    return {
        'text': text,
        'type': 'text',
        'command': command,
        'source': 'BOT',
        'context': context,
        'id': mid
    }

def getNextQuestion(id):
    return Question.objects.get(pk=id)

def getResponseFor(text, command, context, id):
    # validate the text for given context 
    # and either return the same question as ID if check fails
    # or return next question (id+1)
    
    new_id = -1
    if ('start' == command.lower() and id == 0):
        new_id = id + 1
        #create new userInfo object
       # user=UserInfo()
    elif (validateUserResponse(text,context)):  #User response is validated 
        new_id = id + 1 
    else: #user validation failed, repeat the question
        new_id = id 
    
    next_question = getNextQuestion(new_id)
    return createBotMessage(next_question.question_text, "reply", next_question.id, next_question.context)