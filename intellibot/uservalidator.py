import datetime,re
from intellibot.models import UserInfo
from intellibot.utils import searchkey

def validateUserResponse(text, context):
    validator = {
        'NAME' : validate_name,
        'GENDER' : validate_gender,
        'DOB' : validate_DOB,
        'SMOKER': validate_smoker
        }
    return validator.get(context.upper())(text)

def validate_name(text):
    try:
        name = re.search("^[A-z][A-z|\.|\s]+$",text).group(0)
        return True
    except Exception:
        return False

def validate_gender(text):
    try:
        return [True for key in ('MALE','FEMALE','MAN','BOY','GIRL','LADY','M','F') if searchkey(key,text)][0]
    except IndexError:
        False


def validate_smoker(text):
    try:
        return [True for key in ('YES','YEAH','YO','ALWAYS','OCCASIONALLY','OFTEN','Y','NO','NOT','NOPE','NEVER','NOTHING','N') if searchkey(key,text)][0]
    except IndexError:
        False

def validate_DOB(text):
    date_format = '%d-%m-%Y'
    date_string = ""
    try:
        date_capture = (re.search('\d{2}-\d{2}-\d{4}',text))
        date_string  = date_capture.group(0)
        date_obj = datetime.datetime.strptime(date_string, date_format)

        #Check if the date is in future, return false
        now = datetime.datetime.now()
        if (date_obj > now):
            return False
        
        return True
    except Exception:
        return False 