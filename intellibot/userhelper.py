import datetime,re
from intellibot.models import UserInfo

def getUserResponseValue(text, context):
    retriever = {
        'NAME': getName,
        'GENDER': getGender,
        'DOB': getDOB,
        'SMOKER': getSmoker
    }
    return retriever.get(context.upper())(text)

def getName(text):
    return text

def getGender(text):
    try:
        return ['Female' for x in ('FEMALE','LADY','GIRL') if x in text.upper()][0]
    except IndexError:
        return ['Male' for x in ('MALE','BOY','MAN') if x in text.upper()][0]

def getDOB(text):
    date_format = '%d-%m-%Y'
    date_string = ""
    try:
        date_capture = (re.search('\d{2}-\d{2}-\d{4}',text))
        date_string  = date_capture.group(0)
       # date_obj = datetime.datetime.strptime(date_string, date_format)
        return date_string
    except Exception:
        return False 

def getSmoker(text):
    try:
        return ['Smoker' for x in ('YES','YEAH','YO','ALWAYS') if x in text.upper()][0]
    except IndexError:
        return ['Non-Smoker' for x in ('NO','NOPE','NEVER') if x in text.upper()][0]

def getFinalMessage(user):
    print(user)
    message = '{} was born in {} and is a {} and {}'
    return message.format(user.name, user.DOB, user.gender, user.smoker)