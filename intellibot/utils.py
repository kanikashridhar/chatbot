import json
from intellibot.models import Question
#from intellibot.uservalidator import validateUserResponse

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
    
