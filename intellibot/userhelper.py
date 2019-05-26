import datetime,re
from intellibot.models import UserInfo

def getUserResponseValue(text, context):
    retriever = {
        'NAME': getName,
        'GENDER': getGender,
        'DOB': getDOB,
        'SMOKER': isSmoker
    }
    return retriever.get(context.upper())(text)

def getName(text):
    return text

def getGender(text):
    if 'FEMALE' in text.upper():
        return 'Female'
    elif 'MALE' in text.upper():
        return 'Male'
    else:
        return 'N/A'

def getDOB(text):
    date_format = '%d-%m-%Y'
    date_string = ""
    try:
        date_capture = (re.search('\d{2}-\d{2}-\d{4}',text))
        date_string  = date_capture.group(0)
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return date_obj
    except Exception:
        return False 

def isSmoker(text):
    if 'YES' in text.upper():
        return 'Smoker'
    elif 'NO' in text.upper():
        return 'Non-Smoker'

def getFinalMessage(user):
    print(user)
    message = '{} was born in {} and is a {} and {}'
    return message.format(user.name, user.DOB, user.gender, user.smoker)

def getUserBy(uname, udob):
    #TODO - Fix this ?
    return UserInfo.objects.filter(name=uname, DOB=udob)
