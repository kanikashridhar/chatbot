import datetime,re
from intellibot.models import UserInfo

def validateUserResponse(text, context):
    validator = {
        'NAME' : validate_name,
        'GENDER' : validate_gender,
        'DOB' : validate_DOB,
        'SMOKER': validate_smoker
        }
    return validator.get(context.upper())(text)

def validate_name(text):
    return True 

def validate_gender(text):
    if [gen for gen in ('MALE','FEMALE','MAN','BOY','GIRL','LADY') if gen in text.upper()]:
        return True
    return False

def validate_smoker(text):
    if [x for x in ('YES','YEAH','YO','ALWAYS','NO','NOT','NEVER') if x in text.upper()]:
       return True
    return False

def validate_DOB(text):
    date_format = '%d-%m-%Y'
    date_string = ""
    try:
        date_capture = (re.search('\d{2}-\d{2}-\d{4}',text))
        date_string  = date_capture.group(0)
        date_obj = datetime.datetime.strptime(date_string, date_format)
        print(date_obj)
        return True
    except Exception:
        return False 