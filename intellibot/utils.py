import json
from intellibot.models import Question
import re
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
    
def searchkey(key,text):
    try:
       return re.search('\\b'+key+'\\b',text, flags=re.IGNORECASE).group(0)
    except AttributeError:
       return False