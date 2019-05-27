import datetime,re
from intellibot.models import UserInfo
from intellibot.utils import searchkey

def getUserResponseValue(text, context):
    retriever = {
        'NAME': getName,
        'GENDER': getGender,
        'DOB': getDOB,
        'SMOKER': getSmoker
    }
    return retriever.get(context.upper())(text)

def getName(text):
    try:
       name = re.search("^[A-z][A-z|\.|\s]+$",text).group(0)
       return name
    except Exception:
       return False

def getGender(text):
    try:
        return ['Female' for key in ('FEMALE','LADY','GIRL','F') if searchkey(key,text)][0]
    except IndexError:
        return ['Male' for key in ('MALE','BOY','MAN','M') if searchkey(key,text)][0]

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
        return ['Smoker' for key in ('YES','YEAH','YO','ALWAYS','OCCASIONALLY','OFTEN','Y') if searchkey(key,text)][0]
    except IndexError:
        return ['Non-Smoker' for key in ('NO','NOT','NOPE','NEVER','NOTHING','N') if searchkey(key,text)][0]

def getFinalMessage(user):
    print(user)
    message = '{} was born in {} and is a {} and {}'
    return message.format(user.name, user.DOB, user.gender, user.smoker)